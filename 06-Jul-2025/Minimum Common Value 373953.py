# Problem: Minimum Common Value - https://leetcode.com/problems/minimum-common-value/

class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        
        l,r = 0, 0

        while l < len(nums1) and r < len(nums2):
            if nums1[l] > nums2[r]:
                r += 1
            elif nums2[r] > nums1[l]:
                l += 1
            else:
                return nums2[r]
        print(l,r)
        return -1