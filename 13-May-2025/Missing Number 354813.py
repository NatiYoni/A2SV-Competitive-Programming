# Problem: Missing Number - https://leetcode.com/problems/missing-number/description/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        # my_set = set(nums)

        # for i in range(n + 1):
        #    if i not in my_set:
        #     return i

        # ans = (n * (n + 1)) // 2

        # for val in nums:
        #     ans -= val
        
        # return ans

        xor_sum = 0
        xor_nums = 0
        for i,val in enumerate(nums):
            xor_sum ^=  i + 1
            xor_nums ^= val
        
        return xor_sum ^ xor_nums