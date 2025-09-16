# Problem: Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit - https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/description/

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        mx = []
        mn = []

        ans = 0
        l = 0
        for i, val in enumerate(nums):
            heappush(mx,(-val,i))
            heappush(mn, (val,i))

            while abs(mx[0][0]) - mn[0][0] > limit:
                l += 1
                while mx and mx[0][1] < l:
                    heappop(mx)
                while mn and mn[0][1] < l:
                    heappop(mn)
                
                
            
            ans = max(ans, i - l + 1)
                

        return ans