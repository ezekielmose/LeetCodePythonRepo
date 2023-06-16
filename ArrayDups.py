from typing import  List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        nums1.sort()
        nums2.sort()
        curr1 = curr2 = 0
        newArr = []

        while curr1 != len(nums1) and curr2 != len(nums2):
            if nums1[curr1] == nums2[curr2]:
                newArr.append(nums1[curr1])
                curr1 += 1
                curr2 += 1
            if nums1[curr1] > nums2[curr2]:
                curr2 += 1
            else:
                curr1 += 1

        return newArr

if __name__ == '__main__':
    c= Solution()
    print(c.intersect([3,6,2],[2,2,8]))