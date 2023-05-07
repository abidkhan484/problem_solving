#! /home/polymath/.pyenv/shims/python

class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        number = str(n)
        total = 0
        for digit in number:
            total += int(digit)
        if total <= target:
            return 0

        length = len(number)
        total = 0; beautiful_number = 0
        for i in range(length):
            digit = int(number[i])
            if total + digit >= target:
                break
            beautiful_number += (digit * (10 ** (length - i - 1)))
            total += digit

        beautiful_number += (10 ** (length - i))
        return beautiful_number - n

s = Solution()
d = s.makeIntegerBeautiful(16, 6)
print(d)
