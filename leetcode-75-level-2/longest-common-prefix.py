#! /home/polymath/.pyenv/shims/python

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        answer, first_word = "", strs[0]
        idx, smallest_word_length = 0, len(min(strs))
        flag = 1
        while idx < smallest_word_length:
            current = first_word[idx]
            for word in strs:
                if word[idx] != current:
                    flag = 0
                    break
            if flag:
                answer += current
            else:
                break
            idx += 1
        return answer

strs = ["flower","flow","flight"]
s = Solution()
answer = s.longestCommonPrefix(strs)
print(answer)
