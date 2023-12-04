#! /home/polymath/.pyenv/shims/python

import fileinput
import os
import logging
import re

input_file = "./input.txt"
my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, input_file)
logging.basicConfig(level=logging.ERROR)


def make_stack_from_input(lines):
  stack = {}
  length = len([item.strip() for item in lines[-1].split("  ")])

  for item in range(length):
    stack[item+1] = []
  lines.pop()

  for line in lines[::-1]:
    i, j = 0, 4
    for idx in range(length):
      char = line[i:j].strip()
      if char:
        stack[idx+1].append(char)
      i, j = i+4, j+4
  return stack

action_starting_lineno = 0
filtered_lines = []
finput = fileinput.input(files=[path])
for line in finput:
  line = line.rstrip("\n")
  if not line:
    action_starting_lineno = fileinput.lineno()
    break
  line = line.replace( "[", " ").replace("]", " ")
  filtered_lines.append(line)
finput.close()


stack = make_stack_from_input(filtered_lines)
logging.info(stack)

for line in fileinput.input(files=[path]):
  if action_starting_lineno:
    action_starting_lineno -= 1
    continue
  [move, source, destination] = map(int, re.findall(r'\d+', line))
  removable = [stack[source].pop() for _ in range(move)]
  removable.reverse()
  stack[destination].extend(removable)
fileinput.close()

logging.info(stack)

length = len(stack.keys())
final_string = ""
for i in range(length):
  final_string += stack[i+1].pop()

print(final_string)
