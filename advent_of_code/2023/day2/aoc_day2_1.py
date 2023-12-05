#! /home/polymath/.pyenv/shims/python

import fileinput
from os import path
from re import findall

input_file = "./input.txt"
my_path = path.abspath(path.dirname(__file__))
path = path.join(my_path, input_file)

input_array = [line.strip("\n") for line in fileinput.input(files=[path])]
conditions = {'green': 13, 'red': 12, 'blue': 14}

total = 0
for line in input_array:
  gameId = int(findall(r'(\d+):', line)[0])
  games = findall(r'(\d+)\s+(\w+)', line)
  flag = 1
  for cube, color in games:
    cube = int(cube)
    if conditions[color] < cube:
      flag = 0
      break
  if flag:
    total += gameId

print(total)
