# Problem: Find Peak Element - https://leetcode.com/problems/find-peak-element

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        print(nums)
        l = 0
        r = len(nums) - 1

        while l < r:
            m = (l+r)//2

            if  m < len(nums) - 1 and nums[m] > nums[m+1]:
                r = m 
            else:
                l = m + 1
        
        return r