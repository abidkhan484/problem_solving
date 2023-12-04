#! /home/polymath/.pyenv/shims/python

import fileinput
from os import path
from re import findall

input_file = "./input.txt"
my_path = path.abspath(path.dirname(__file__))
path = path.join(my_path, input_file)

input_array = [line.strip('\n') for line in fileinput.input(files=[path])]

output = 0
for line in input_array:
  numbers = findall(r'\d', line)
  output += int(numbers[0] + numbers[-1])

print(output)

