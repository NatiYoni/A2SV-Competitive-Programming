# Problem: Sort Colors - https://leetcode.com/problems/sort-colors/

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        for i in range(len(nums)-1):
            j = i + 1

            while nums[j] < nums[i] and j > 0 :
                print(i)
                print(j)
                nums[i], nums[j] = nums[j], nums[i]
                j -= 1
                i -= 1

        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[j] < nums[i]:
        #             nums[i], nums[j] = nums[j], nums[i]