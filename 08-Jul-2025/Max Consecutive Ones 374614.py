# Problem: Max Consecutive Ones - https://leetcode.com/problems/max-consecutive-ones/

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = cnt = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                cnt = 0
            else:
                cnt += 1 
                
            ans = max(cnt,ans)
        
        return ans

