#! /home/polymath/.pyenv/shims/python

from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = [0] * 3
        for num in nums:
            counter[num] += 1
        
        for i in range(len(nums)):
            if counter[0]:
                num = 0
                counter[0] -= 1
            elif counter[1]:
                num = 1
                counter[1] -= 1
            else:
                num = 2
            nums[i] = num



nums = [2,0,2,1,1,0]
# nums = [2,0,1]
s = Solution()
s.sortColors(nums)
print(nums)
