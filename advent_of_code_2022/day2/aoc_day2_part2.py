#! /home/polymath/.pyenv/shims/python

import fileinput
import os

input_file = "./input.txt"
my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, input_file)

opponent = ['A', 'B', 'C']; me = ['X', 'Y', 'Z']
choose_point = {'X': 1, 'Y': 2, 'Z':3}
game_result = {'X': 0, 'Y': 3, 'Z': 6}


total_count = 0
for line in fileinput.input(files=[path]):
  [opponent_choose, my_choose_predicted] = line.rstrip('\n').split(' ')
  [opponent_index, my_predicted_choose_index] = [opponent.index(opponent_choose), me.index(my_choose_predicted)]
  total_count += game_result[my_choose_predicted]

  my_choose = ((my_predicted_choose_index + opponent_index - 1) % 3)
  total_count += choose_point[me[my_choose]]

print(total_count)
