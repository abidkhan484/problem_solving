#! /home/polymath/.pyenv/shims/python

import fileinput
import os
import logging

input_file = "./short_input.txt"
my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, input_file)
logging.basicConfig(level=logging.INFO)

current_path = ""
directories = {}
for line in fileinput.input(files=[path]):
  line = line.rstrip("\n")
  if line[0] == "$":
    command = line[1]
    if command == "cd":
      if line[2] == "..":
        current_path = current_path.rsplit("/", 1)[0]
      else:
        current_path += line[3]
    elif command == "ls":
      pass


fileinput.close()


