import sys

if len(sys.argv) < 2:
    print("Please pass in a second filename: python3 in and out.py second_filename.py")
    sys.exit()

file_name = sys.argv[1]
try:
    with open(file_name) as file:
        for line in line:
            splt_line = line.split('#')[0]
            command = splt_line.strip()

            if command == '':
                continue

            num = int(command, 2)

            print(f'{num8b} is {num}')


except FileNotFoundError:
    print(f'{sys.argv[0]: sys.argv[1]} file was not found')
