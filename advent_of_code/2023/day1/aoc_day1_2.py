#! /home/polymath/.pyenv/shims/python

import fileinput
from os import path
from re import findall

input_file = "./input.txt"
my_path = path.abspath(path.dirname(__file__))
path = path.join(my_path, input_file)

input_array = [line.strip('\n') for line in fileinput.input(files=[path])]

number_key_value = {'nine': '9', 'eight': '8', 'seven': '7', 'six': '6',
  'five': '5', 'four': '4', 'three': '3', 'two': '2', 'one': '1'}
pattern = '|'.join(number_key_value.keys()) + '|' + '\d'
pattern = '(?=('+'|'.join(number_key_value.keys())+'|\\d))'

output = 0
for line in input_array:
  numbers = findall(pattern, line)
  numbers = [number_key_value[number] if number in number_key_value else number for number in numbers]
  output += int(numbers[0] + numbers[-1])

print(output)

