#!/usr/bin/env python3

"""Main."""

import sys

LDI = 0b10000010
HLT = 0b00000001
PRN = 0b01000111
MUL = 0b10100010
ADD = 0b10100000
PUSH = 0b01000101
POP = 0b01000110
CALL = 0b01010000
RET = 0b00010001
CMP = 0b10100111
JMP = 0b01010100
JEQ = 0b01010101
JNE = 0b01010110


class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.ram = [0] * 256
        self.reg = [0] * 8
        self.pc = 0
        self.mar = []
        self.mdr = []
        self.fl = []
        self.branchtable = {}
        self.branchtable[LDI] = self.handle_ldi
        self.branchtable[PRN] = self.handle_prn
        self.branchtable[MUL] = self.handle_mul
        self.branchtable[PSH] = self.handle_psh
        self.branchtable[POP] = self.handle_pop

    def handle_ldi(self, a, b):
        self.reg[a] = b
        self.pc += 2

    def handle_prn(self, a):
        print(self.reg[a])
        self.pc += 2

    def handle_mul(self, a, b):
        self.alu("MUL", a, b)
        self.pc += 2

    def handle_psh(self, a):
        # decrement the stack pointer
        self.reg[7] -= 1

        # get the register number

        value = self.reg[a]

        sp = self.reg[7]

        self.ram[sp] = value

        self.pc += 1

    def handle_pop(self, a):
        sp = self.reg[7]

        value = self.ram[sp]

        # put the value into the given register
        self.reg[a] = value
        # increment our stack pointer

        self.reg[7] += 1

        self.pc += 1

    def load(self):
        """Load a program into memory."""

        try:
            address = 0
            with open(file_name) as file:
                for line in line:
                    splt_line = line.split('#')[0]
                    command = splt_line.strip()

                    if command == '':
                        continue

                    instruction = int(command, 2)
                    memory[address] = instruction

                    address += 1

        except FileNotFoundError:
            print(f'{sys.argv[0]: sys.argv[1]} file was not found')
            sys.exit()

    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        elif op == "MUL":
            self.reg[reg_a] *= self.reg[reg_b]
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            # self.fl,
            # self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""
        running = True

        while running:

            IR = self.ram_read(self.pc)
            operand_a = self.ram_read(self.pc + 1)
            operand_b = self.ram_read(self.pc + 2)

            if IR >> 6 == 2:
                self.branchtable[IR](operand_a, operand_b)

            if (IR >> 6) == 1:
                self.branchtable[IR](operand_a)

            if IR == HLT:
                running = False

            # if IR == PRN:
            #     print(self.reg[operand_a])
            #     self.pc += 1

            # if IR == ADD:
            #     self.alu("ADD", operand_a, operand_b)
            #     self.pc += 2

            # if IR == MUL:
            #     self.alu("MUL", operand_a, operand_b)
            #     self.pc += 2

        self.pc += 1

    def ram_read(self, mar):
        # should accept the address to read and return the value stored there.
        if MAR < len(self.ram):
            return self.ram[MAR]
        else:
            return None

    def ram_write(self, value, address):
        self.ram[address] = value

        return value


cpu = CPU()

file = sys.argv[1]

if len(sys.argv) < 2:
    print(
        "Please pass in a second filename: python3 in_and_out.py second_filename.py")
    sys.exit()

cpu.load(file)
cpu.run()
