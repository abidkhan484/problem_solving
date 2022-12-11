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

    first_number_of_left, second_number_of_left = map(int, left.strip().split("-"))
    first_number_of_right, second_number_of_right = map(int, right.strip().split("-"))

    first_condition = (first_number_of_left <= first_number_of_right
        and second_number_of_left >= second_number_of_right)
    second_condition = (first_number_of_left >= first_number_of_right
        and second_number_of_left <= second_number_of_right)

    logging.info(f"Here line {line} in line no {fileinput.lineno()} where first condition {first_condition} and second {second_condition}")

    if first_condition or second_condition:
        total += 1

print(total)
