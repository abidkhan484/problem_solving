#! /home/polymath/.pyenv/shims/python
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currentSum = 0
        maximum = -10001
        for num in nums:
            currentSum += num
            if currentSum > maximum:
                maximum = currentSum
            if currentSum < 0:
                currentSum = 0
        return maximum

s = Solution()
nums = [-2,-1]
maxSubArray = s.maxSubArray(nums)
print(maxSubArray)
