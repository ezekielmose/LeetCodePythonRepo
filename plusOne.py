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
        for i in range(len(digits)-1,-1,-1):
            if digits[i]<9:
                digits[i]+=1
                return digits
            digits[i]=0

        return [1]+[0]*len(digits)
if __name__=='main':
    r=Solution
    print(r.plusOne(1,1,2,3,1))