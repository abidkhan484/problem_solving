#! /home/polymath/.pyenv/shims/python

import fileinput
import os
import logging
from collections import deque

input_file = "./input.txt"
my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, input_file)
logging.basicConfig(level=logging.ERROR)

queue_maxsize = 4

for line in fileinput.input(files=[path]):
  line = line.rstrip("\n")
fileinput.close()

q = deque([], maxlen=queue_maxsize)
char_index = 0
for char in line:
  if len(set(q)) == queue_maxsize:
    break
  q.append(char)
  char_index += 1

print(char_index)
