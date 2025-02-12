# Problem: Move Zeroes - https://leetcode.com/problems/move-zeroes/

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index , non_zero = 0 , 0
        while index < len(nums):

            if nums[index] != 0:
                nums[index], nums[non_zero] = nums[non_zero] , nums[index] 

                non_zero += 1

            index += 1 