# Problem: Longest Nice Subarray - https://leetcode.com/problems/longest-nice-subarray/

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:

        ans = 0
        val = 0
        left = 0
        for right in range(len(nums)):
            
            while val & nums[right] != 0:
                val ^= nums[left]
                left += 1
               
        
            val |= nums[right]
            ans = max(ans, right - left + 1)

        return ans
