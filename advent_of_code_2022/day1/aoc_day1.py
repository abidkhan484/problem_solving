#! /home/polymath/.pyenv/shims/python

import fileinput
import os

input_file = "./input.txt"
my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, input_file)

maximum = -1
current = 0
for line in fileinput.input(files=[input_file]):
  if line == '\n':
    maximum = max(current, maximum)
    current = 0
    continue
  current += int(line)

print(maximum)  
