#! /home/polymath/.pyenv/shims/python

from typing import List
from collections import Counter

class Solution:
  def maxOperations(self, nums: List[int], k: int) -> int:
    nums_table = Counter(nums)
    unique_numbers = sorted(nums_table)
    i, j = 0, len(unique_numbers)-1

    final_counter = 0
    if (not k&1) and (k//2 in nums_table):
      final_counter += (nums_table[k//2] // 2)
    while i < j:
      x = unique_numbers[i]
      y = unique_numbers[j]
      summation = x + y
      if summation == k:
        final_counter += min(nums_table[x], nums_table[y])
        i += 1; j -= 1
      elif summation > k:
        j -= 1
      else:
        i += 1
    return final_counter

s = Solution()
nums = [3,1,3,4,3,2]
k = 6
print(s.maxOperations(nums, k))
