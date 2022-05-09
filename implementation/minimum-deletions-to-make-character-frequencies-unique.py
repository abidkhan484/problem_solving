#! /home/polymath/.pyenv/shims/python

from collections import Counter

class Solution:
    def minDeletions(self, s: str) -> int:
        char_dictionary = dict()
        deleted_char_count = 0
        for char in s:
            if char not in char_dictionary:
                char_dictionary[char] = 0
            char_dictionary[char] += 1

        values = list(char_dictionary.values())
        values.sort(reverse=True)

        length = len(values)
        for i in range(length):
            value = values[i]
            count = 0
            while True:
                if value and value in values[i+1:]:
                    value -= 1
                    deleted_char_count += 1
                    count += 1
                else:
                    if count:
                        values.append(value)
                    break
        return deleted_char_count
            























        # if length <= 1:
        #     return 0
        # for i in range(length-1):
        #     value = values[i]
        #     if value not in values:
        #         continue
        #     occuerences = values.count(value)
        #     k = i + occuerences - 1
        #     for j in range(k, length):
        #         pass




string = input().strip()
s = Solution()
print(s.minDeletions(string))

