#! /home/polymath/.pyenv/shims/python
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        minValue = prices[0]
        maxValue = 0
        length = len(prices)
        for i in range(1, length):
            val = prices[i] - minValue
            if val < 0:
                minValue = prices[i]
            elif val > maxValue:
                maxValue = val

        return maxValue


prices = [7,1,5,3,6,4]
s = Solution()
maxProfit = s.maxProfit(prices)
print(maxProfit)
