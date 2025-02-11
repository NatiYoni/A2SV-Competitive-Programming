# Problem: Largest Number - https://leetcode.com/problems/largest-number/

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                p1 = str(nums[i]) + str(nums[j])
                p2 =  str(nums[j]) + str(nums[i])

                if int(p1) < int(p2):
                    nums[i], nums[j] = nums[j], nums[i]

        for index, num in enumerate(nums):
            nums[index] = str(num)
        
        result = "".join(nums)

        return str(int(result))