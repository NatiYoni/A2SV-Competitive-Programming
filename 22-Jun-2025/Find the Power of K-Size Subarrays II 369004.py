# Problem: Find the Power of K-Size Subarrays II - https://leetcode.com/problems/find-the-power-of-k-size-subarrays-ii/

class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        mx = 0
        n = len(nums)

        stack = []
        ans = []
        cnt = 0
        for i,val in enumerate(nums):
            if stack:
                if val == stack[-1] + 1: 
                    stack.append(val)
                else:
                    stack.clear()

            if not stack:
                stack.append(val)
            
            if i >= k - 1:
                if len(stack) >= k:
                    ans.append(stack[-1])
                else:
                    ans.append(-1)
        
        return ans
