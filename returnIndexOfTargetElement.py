from  typing import List

class TargetElement:
    def returnTarget(self, nums:List[int], target: int)->int:
        l = 0
        r = len(nums)

        while l < r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            if nums[m] < target:
                l = m + 1
            else:
                r = m
        return l

if __name__=='__main__':
    r=TargetElement()
    print(r.returnTarget([2,3,4,5,6,7],5))