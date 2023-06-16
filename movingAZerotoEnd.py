from typing import List
class MoveZero:
    def moveZeros(self, nums: List[int]):

        j=0

        for num in nums:
            if num != 0:
                nums[j] =num
                j+=1
        for i in range (j, len(nums)):
            nums[i] =0

if __name__ =='__main__':
    c=MoveZero()
    print(c.moveZeros([3,0,2,1,4,0,5]))

