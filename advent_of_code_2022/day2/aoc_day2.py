#! /home/polymath/.pyenv/shims/python

import fileinput
import os

input_file = "./input.txt"
my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, input_file)

opponent = ['A', 'B', 'C']; me = ['X', 'Y', 'Z']
choose_point = {'X': 1, 'Y': 2, 'Z':3}
game_result = {'lost': 0, 'draw': 3, 'win': 6}
game_result_keys = list(game_result.keys())

total_count = 0
for line in fileinput.input(files=[path]):
  [opponent_choose, my_choose] = line.rstrip('\n').split(' ')
  [opponent_index, my_choose_index] = [opponent.index(opponent_choose), me.index(my_choose)]
  total_count += choose_point[my_choose]

  result = ((my_choose_index - opponent_index + 1) % 3)
  total_count += game_result[game_result_keys[result]]

print(total_count)
