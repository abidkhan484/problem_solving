#! /home/polymath/.pyenv/shims/python

class Solution:
  def maxVowels(self, s: str, k: int) -> int:
    vowels = {'a', 'e', 'i', 'o', 'u'}
    length = len(s)
    count = 0
    for i in range(k):
      count += s[i] in vowels

    j = i + 1; p = 0; maximum = count
    for i in range(j, length):
      count -= s[p] in vowels
      count += s[i] in vowels
      maximum = max(count, maximum)
      p += 1

    return maximum

s = Solution()
string = "abciiidef"
k = 3
string = "ibpbhixfiouhdljnjfflpapptrxgcomvnb"
k = 33
print(s.maxVowels(string, k))
