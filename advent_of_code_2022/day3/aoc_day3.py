#! /home/polymath/.pyenv/shims/python

import fileinput
import os
import string

input_file = "./input.txt"
my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, input_file)

total = 0
characters = {}
i = 1
for char in string.ascii_letters:
  characters[char] = i
  i += 1

for line in fileinput.input(files=[path]):
  line = line.rstrip('\n')
  middle = len(line) // 2
  left, right = set(list(line[middle:])), set(list(line[:-middle]))
  for char in left:
    if char in right:
      total += characters[char]

print(total)

