# Problem: House Robber IV - https://leetcode.com/problems/house-robber-iv/

class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        
        def check(m):

            count = 0
            i = 0
            while i < len(nums):
                if nums[i] <= m:
                    count += 1
                    i += 2
                else:
                    i += 1
            return count >= k 

            pass
        
        l = min(nums)
        h = max(nums)


        while l <= h :

            m = l + ( h - l)//2

            if check(m):
                h = m - 1
            else:
                l = m + 1
        
        return h + 1
