# Problem: Product of Array Except Self - https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        result = [1] * len(nums)

        suffix = 1
        for i in range(len(nums)-1,-1,-1):
            suffix *= nums[i]
            result[i] = suffix
        

        prefix = 1
        result[0] = result[1]
        for i in range(1,len(nums)):
            prefix *= nums[i-1]
            if i < len(nums) -1 :
                result[i] =result[i + 1] * prefix
            else:
                result[i] = prefix

        
        return result
