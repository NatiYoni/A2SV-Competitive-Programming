# Problem: Python Check if All the Integers in a Range Are Covered - https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/description/

class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:

        sor = list(zip(nums, cost))
        sor.sort()
        
        prefix = [0] * len(nums)
        running_sum = 0

        for i in range(1,len(nums)):
            running_sum += sor[i-1][1]
            prefix[i] =  prefix[i-1] + running_sum * (sor[i][0] - sor[i-1][0])
        
        
        suffix =  [0] * len(nums)
        running_sum = 0

        for i in range(len(nums)-2,-1,-1):
            running_sum += sor[i+1][1]
            suffix[i] =  suffix[i+1] + running_sum * abs(sor[i][0] - sor[i+1][0])

        costs = [0] * len(nums)
        for i in range(len(nums)):
            costs[i] = suffix[i] + prefix[i]

        return min(costs) 

      
