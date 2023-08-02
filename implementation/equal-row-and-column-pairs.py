#! /home/polymath/.pyenv/shims/python

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        columns = list(map(list, zip(*grid)))
        length = len(grid)
        pairs = 0
        for i in range(length):
            for j in range(length):
                if grid[i] == columns[j]:
                    pairs += 1
        return pairs
