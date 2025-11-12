# Problem: Sum of All Subset XOR Totals - https://leetcode.com/problems/sum-of-all-subset-xor-totals/

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def dp(i,cur):
            if i >= len(nums):
                return cur

            take = dp(i+1,cur^nums[i])
            leave = dp(i+1, cur) 
            return take + leave 

        return dp(0,0)