# Problem: Longest Subarray of 1's After Deleting One Element - https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        dq = deque()
        l = 0
        ans = 0
      
        for i in range(n):
            if nums[i] == 0:
                dq.append(i)
            if len(dq) == 2:
                l = dq.popleft() + 1
            
            ans = max(ans, i - l)
        
        return ans
            

