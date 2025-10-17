# Problem: Min Cost Climbing Stairs - https://leetcode.com/problems/min-cost-climbing-stairs/

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        a,b = cost[0],cost[1]

        for i in range(2,len(cost)):
            a,b = b, min(a+cost[i],b+cost[i])
        
        return min(a,b)