from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:


        # m= len(nums1) #[2,4,3]     #3
        # n= len(nums2)   #[5,2,1]    #3



        mid=(nums1 + nums2).sort()

        for num in range(mid):
            midian=mid/2



