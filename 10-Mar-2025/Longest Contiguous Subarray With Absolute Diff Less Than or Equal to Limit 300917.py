# Problem: Longest Contiguous Subarray With Absolute Diff Less Than or Equal to Limit - https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        
        dq_max = deque()
        dq_min = deque()
        ans = float("-inf")

        l = 0
        
        for i in range(len(nums)):
        
            while dq_max and dq_max[-1] < nums[i]:
                dq_max.pop()
            
            while dq_min and dq_min[-1] > nums[i]:
                dq_min.pop()

            dq_max.append(nums[i])
            dq_min.append(nums[i])

            while dq_max and dq_min and abs(dq_max[0] - dq_min[0]) > limit:

                if dq_max[0] == nums[l]:
                    dq_max.popleft()
                    

                if dq_min[0] == nums[l]:
                    dq_min.popleft()
                   
            
                l += 1
            
    
            ans = max(ans, i - l + 1)
        return ans 
