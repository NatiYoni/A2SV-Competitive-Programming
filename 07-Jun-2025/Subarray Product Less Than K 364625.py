# Problem: Subarray Product Less Than K - https://leetcode.com/problems/subarray-product-less-than-k/

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:

        if k <= 1:
            return 0
        
        l = 0
        ans = 0
        multi = 1

        for i in range(len(nums)):
            multi *= nums[i]
            while multi >= k:
                multi //= nums[l]
                l += 1
            
            
            # print(i,l)
            ans += i - l + 1 

        return ans 
            
