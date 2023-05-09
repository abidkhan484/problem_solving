#! /home/polymath/.pyenv/shims/python

from typing import List

class Solution:
  def compress(self, chars: List[str]) -> int:
    length = len(chars)
    if length == 1:
      return 1
    i = 0; final_length = 0
    while i < length:
      char = chars[i]
      total = 0
      for j in range(i+1, length):
        if chars[j] != char:
          break
        total += 1
      else:
        j += 1

      i = j
      chars[final_length] = char
      final_length += 1
      if total:
        total = str(total+1)
        for s in total:
          chars[final_length] = s
          final_length += 1

    return final_length

s = Solution()
# chars = ["a","b","c","c"]
chars = ["a","a","b","b","c","c","c"]
chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
print(s.compress(chars))
