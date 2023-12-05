#! /home/polymath/.pyenv/shims/python

import fileinput
from os import path
from re import findall
from functools import reduce

input_file = "./input.txt"
my_path = path.abspath(path.dirname(__file__))
path = path.join(my_path, input_file)

input_array = [line.strip("\n") for line in fileinput.input(files=[path])]

total = 0
for line in input_array:
  games = findall(r'(\d+)\s+(\w+)', line)
  colors = {'green': 1, 'red': 1, 'blue': 1}
  for cube, color in games:
    colors[color] = max(int(cube), colors[color])

  total += reduce(lambda x, y: x*y, colors.values(), 1)

print(total)
