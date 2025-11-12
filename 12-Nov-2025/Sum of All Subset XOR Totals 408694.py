# Problem: Sum of All Subset XOR Totals - https://leetcode.com/problems/sum-of-all-subset-xor-totals/

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0
        for val in nums:
            res|=val
        
        return res * 2**(len(nums)-1)