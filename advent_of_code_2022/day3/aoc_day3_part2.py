#! /home/polymath/.pyenv/shims/python

import fileinput
import os
import string
import logging

input_file = "./input.txt"
my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, input_file)
logging.basicConfig(level=logging.ERROR)

total = 0
characters = {}
i = 1
for char in string.ascii_letters:
  characters[char] = i
  i += 1

no_of_line_in_set = 3
lines = []; line_no = 0
for line in fileinput.input(files=[path]):
  line = line.rstrip('\n')
  line_no += 1

  if line_no <= no_of_line_in_set:
    lines.append(line)

  if line_no == no_of_line_in_set:
    matched_char = set.intersection(*map(set, lines))
    for char in matched_char:
      total += characters[char]

    logging.info("Final lines " + ", ".join(lines))
    lines = []
    line_no = 0

  logging.info(f"line no {line_no} where line {line}")

print(total)

