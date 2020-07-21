#!/usr/bin/env python3

"""Main."""

import sys
from cpu import *

cpu = CPU()

file = sys.argv[1]

if len(sys.argv) < 2:
    print(
        "Please pass in a second filename: python3 in_and_out.py second_filename.py")
    sys.exit()

cpu.load(file)
cpu.run()
