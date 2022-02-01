#! /home/polymath/.pyenv/shims/python
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) > len(set(nums))

s = Solution()
nums = [1,2,3,4]
checkDuplicate = s.containsDuplicate(nums)
print(checkDuplicate)