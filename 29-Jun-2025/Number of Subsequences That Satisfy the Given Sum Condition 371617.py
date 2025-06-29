# Problem: Number of Subsequences That Satisfy the Given Sum Condition - https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        print(nums)
        ans = 0

        for i,num in enumerate(nums):
            temp = target - num
            right = bisect_right(nums,temp) - 1

            if right >= i:
                ans += 2**(right - i)

            
            
            
        
        return ans % (10**9 + 7)

        

