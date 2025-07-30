# Problem: Longest Subarray With Maximum Bitwise AND - https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ans = 0
        mx = 1
        length = 0
        
        for val in nums:
            if val > mx:
                mx = val
                length = 1
                ans = 1
            elif val == mx:
                length += 1
            else:
                length = 0

            ans = max(ans,length)
        
        return ans