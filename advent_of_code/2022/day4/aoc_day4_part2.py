#! /home/polymath/.pyenv/shims/python

import fileinput
import os
import logging

input_file = "./input.txt"
my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, input_file)
logging.basicConfig(level=logging.ERROR)

total = 0
for line in fileinput.input(files=[path]):
    line = line.rstrip("\n")
    left, right = line.split(",")

    first_number_of_left, second_number_of_left = map(
        int, left.strip().split("-"))
    first_number_of_right, second_number_of_right = map(
        int, right.strip().split("-"))

    condition = max(
        max(first_number_of_left, first_number_of_right)
        - min(second_number_of_left, second_number_of_right),
        0
    )
    if not condition:
        logging.info(f"Condition is fulfilled in line {line} which line no {fileinput.lineno()} where condition is {condition}")
        total += 1

print(total)
