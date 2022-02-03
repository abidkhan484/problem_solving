#! /home/polymath/.pyenv/shims/python

from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        i, j = 0, len(nums)-1
        while i != j:
            p = ((i+j)//2)
            if nums[p] < nums[j]:
                j = p
            else:
                i = p+1
        return nums[i]

s = Solution()
nums = [2,3,4,5,1]
minimum = s.findMin(nums)
print(minimum)
