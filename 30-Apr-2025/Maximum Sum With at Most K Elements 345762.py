# Problem: Maximum Sum With at Most K Elements - https://leetcode.com/problems/maximum-sum-with-at-most-k-elements/description/

class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        arr = [0 for _ in range(len(grid))]


        def helper(grid,l):
            heapify(grid)
            
            temp = len(grid) - l
            while temp > 0:
                heappop(grid)
                temp -= 1
            
            return  grid

        
        res = []
        for i,val in enumerate(grid):
            res.extend(helper(val,limits[i]))

        # print(res)
        temp = len(res) - k
        heapify(res)
        while temp > 0:
            temp -= 1
            heappop(res)
        
        # print(res)
        return sum(res)
        

