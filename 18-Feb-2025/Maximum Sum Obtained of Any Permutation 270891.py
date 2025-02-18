# Problem: Maximum Sum Obtained of Any Permutation - https://leetcode.com/problems/maximum-sum-obtained-of-any-permutation/description/

class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        nums.sort(reverse = True)
        sweaper = [0] * (len(nums)+1)

        for start, end in requests:
            sweaper[start] += 1
            sweaper[end + 1] -= 1 
        
        for i in range(1,len(nums)):
            sweaper[i] += sweaper[i - 1]

        sweaper.sort(reverse = True)


        output = 0
        for i in range(len(nums)):
            output += nums[i] * sweaper[i]

        return output % (10**9 + 7)