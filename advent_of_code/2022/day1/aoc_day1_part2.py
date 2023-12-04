#! /home/polymath/.pyenv/shims/python

import fileinput
import logging
import os

logging.basicConfig(level=logging.ERROR)

input_file = "./input.txt"
my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, input_file)

maximum = [0] * 3
current = 0
for line in fileinput.input(files=[path]):
  line = line.rstrip('\n')
  if not line:
    if current > maximum[-1]:
      maximum.pop()
      maximum.append(current)
      maximum.sort(reverse=True)
    current = 0
    continue
  logging.info(f"line no {fileinput.lineno()} with value {line} and type {type(line)} that is boolean {bool(line)} where current value is {current}")
  current += int(line)
else:
  if current > maximum[-1]:
    maximum.pop()
    maximum.append(current)

print(sum(maximum))
