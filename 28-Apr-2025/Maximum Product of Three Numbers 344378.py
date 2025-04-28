# Problem: Maximum Product of Three Numbers - https://leetcode.com/problems/maximum-product-of-three-numbers/description/

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort(reverse = True)

        ans1 = nums[0] * nums[1] * nums[2]
        ans2 =  nums[-1] * nums[-2] * nums[0]
        ans3 =  nums[-1] * nums[-2] * nums[-3]
        
        
        return max(ans1,ans2,ans3)
