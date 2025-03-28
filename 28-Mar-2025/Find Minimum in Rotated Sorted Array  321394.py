# Problem: Find Minimum in Rotated Sorted Array  - https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l = 0
        r = len(nums) - 1

        if nums[l] < nums[r]:
            return nums[0]

        while l < r:

            m = l + (r - l) // 2

            if nums[m] > nums[r]:
                l = m + 1
            
            else:
                r = m 
        
        return nums[l]
            
