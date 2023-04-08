#! /home/polymath/.pyenv/shims/python

from typing import List

class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        column, row = len(grid[0]), len(grid)
        answer = [-1] * column
        for idx in range(column):
            i, j = 0, idx
            blocked = 0
            while not blocked and i != row:
                item = grid[i][j]
                if item == 1:
                    p = j + 1
                    if p == column:
                        blocked = 1
                        break
                else:
                    p = j - 1
                    if p < 0:
                        blocked = 1
                        break
                if not (item + grid[i][p]):
                    blocked = 1
                    break
                i, j = i+1, p
            answer[idx] = -1 if blocked else j
        return answer


grid = [[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]
s = Solution()
answer = s.findBall(grid)
print(answer)
