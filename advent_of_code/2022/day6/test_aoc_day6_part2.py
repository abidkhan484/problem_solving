#! /home/polymath/.pyenv/shims/python

import pytest
from aoc_day6_part2 import get_start_of_message_index


@pytest.mark.parametrize("test_input, expected", [
    ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 19),
    ("bvwbjplbgvbhsrlpgdmjqwftvncz", 23),
    ("nppdvjthqldpwncqszvftbrmjlhg", 23),
    ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 29),
    ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 26),
])
def test_get_start_of_message_index(test_input, expected):
    assert get_start_of_message_index(test_input) == expected
