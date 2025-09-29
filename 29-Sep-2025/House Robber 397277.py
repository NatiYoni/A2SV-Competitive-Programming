# Problem: House Robber - https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:

        a , b = 0 , nums[0]

        for i in range(1, len(nums)):

            temp = b

            b = max(a + nums[i],b)

            a  = temp
        return b