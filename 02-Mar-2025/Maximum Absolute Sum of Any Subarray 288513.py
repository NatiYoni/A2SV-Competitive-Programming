# Problem: Maximum Absolute Sum of Any Subarray - https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        n = len(nums)
        
        cur = 0
        max_ = nums[0]

        for i in range(n):
            cur += nums[i]

            if max_ < cur:
                max_ = cur
            
            if cur <= 0:
                cur = 0
            
        # print(max_)
        min_ = nums[0]
        cur = 0

        for i in range(n):
            cur += nums[i]

            if min_ > cur:
                min_ = cur
            
            if cur >= 0:
                cur = 0

        # print(min_)
        return max(abs(max_), abs(min_))



            

