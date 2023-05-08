#! /home/polymath/.pyenv/shims/python

class Solution:
  def reverseVowels(self, s: str) -> str:
    string = list(s)
    length = len(s)
    vowels = 'aAeEiIoOuU'

    vowel_positions = []
    for i in range(length):
      char = string[i]
      if char in vowels:
        vowel_positions.append(i)

    vowel_length = len(vowel_positions)
    vowel_iteration = (vowel_length + 1) // 2
    i, j = 0, vowel_length - 1
    for _ in range(vowel_iteration):
      x, y = vowel_positions[i], vowel_positions[j]
      string[x], string[y] = string[y], string[x]
      i += 1; j -= 1

    return ''.join(string)

s = Solution()
string = "a"
print(s.reverseVowels(string))
