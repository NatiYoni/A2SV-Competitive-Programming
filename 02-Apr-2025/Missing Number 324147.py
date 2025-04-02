# Problem: Missing Number - https://leetcode.com/problems/missing-number/description/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        length = len(nums)
        my_set = set(nums)

        for i in range(length + 1):
           if i not in my_set:
            return i