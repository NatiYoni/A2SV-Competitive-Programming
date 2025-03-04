# Problem: Two City Scheduling - https://leetcode.com/problems/two-city-scheduling/

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:

        diff = defaultdict(int)
        for i in range(len(costs)):
            diff[i] = costs[i][0] - costs[i][1]
        
        ans = dict(sorted(diff.items(), key = lambda x: x[1]))
        
        i = 1
        total = 0
        for index in ans.keys():
            if i <= len(costs) // 2:
                total += costs[index][0]
            else:
                total += costs[index][1]
            
            i += 1
        
        return total




        # print(ans)
        # # print(diff)
        
        # # return total


