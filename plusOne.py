"""class Solution(object):
  def plusOne(self, digits):

        digit_length = len(digits)

        i = digit_length - 1

        while digits[i] == 9 and i >= 0:
            i -= 1

        if i == -1:
            results = [0] * (digit_length + 1)
            results[0] = 1
            return results

        results = [0] * (digit_length)

        results[i] = digits[i] + 1

        for j in range(i - 1, -1, -1):
            results[j] = digits[j]

        return results
if __name__=='maim':
    r=Solution
    print(r.plusOne([1,1,2,0,1]))

"""
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        for i in range(n - 1, -1, -1):
            digits[i] += 1
            digits[i] %= 10
            if digits[i] != 0:
                return digits
        return [1] + digits
if __name__=='main':
    r=Solution
    print(r.plusOne(1,1,2,3,1))