# Problem: House Robber - https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def rob(i):
            if i < 0:
                return 0

            if i in memo:
                return memo[i]

            val = 0
            val +=  max(rob(i-2), rob(i-3)) + nums[i]
            memo[i] = val 
            return val
        
        
        return max(rob(len(nums) - 1), rob(len(nums) - 2))