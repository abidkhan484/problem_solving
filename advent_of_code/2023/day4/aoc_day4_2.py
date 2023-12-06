#! /home/polymath/.pyenv/shims/python

import fileinput
from os import path
from collections import Counter
from re import findall


input_file = "./input.txt"
my_path = path.abspath(path.dirname(__file__))
path = path.join(my_path, input_file)

input_array = [line.strip("\n") for line in fileinput.input(files=[path])]

cards = []
for line in input_array:
  _, numbers = line.split(":")
  winning_numbers, card_numbers = numbers.split("|")

  winning_numbers  = Counter(findall(r'\d+', winning_numbers))
  card_numbers = Counter(findall(r'\d+', card_numbers))
  winning_numbers_set = set(winning_numbers.keys())
  card_numbers_set = set(card_numbers.keys())

  total_matched = sum(min(winning_numbers[number], card_numbers[number]) for number in winning_numbers_set & card_numbers_set)
  cards.append(total_matched)

length = len(cards)
c_list = [1] * length
for i in range(length):
  if not cards[i]:
    continue
  for j in range(i+1, min(i + 1 + cards[i], length)):
    c_list[j] += c_list[i]

print(sum(c_list))


