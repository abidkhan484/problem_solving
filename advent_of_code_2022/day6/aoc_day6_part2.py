#! /home/polymath/.pyenv/shims/python

import fileinput
import os
import logging
from collections import deque

input_file = "./input.txt"
my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, input_file)
logging.basicConfig(level=logging.ERROR)

queue_maxsize = 14

def get_start_of_message_index(line):
  q = deque([], maxlen=queue_maxsize)
  char_index = 0
  for char in line:
    if len(set(q)) == queue_maxsize:
      break
    q.append(char)
    char_index += 1

  return char_index


for line in fileinput.input(files=[path]):
  line = line.rstrip("\n")
fileinput.close()

char_index = get_start_of_message_index(line)
print(char_index)
