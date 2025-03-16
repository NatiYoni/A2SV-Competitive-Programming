# Problem: Number of Good Pairs - https://leetcode.com/problems/number-of-good-pairs/

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        counter = Counter(nums)

        ans = 0
        for val in counter.values():

            ans += (val - 1)*(val)//2
        
        return ans
