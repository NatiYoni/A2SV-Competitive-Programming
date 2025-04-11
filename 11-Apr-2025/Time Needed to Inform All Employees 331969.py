# Problem: Time Needed to Inform All Employees - https://leetcode.com/problems/time-needed-to-inform-all-employees/

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = defaultdict(list)
        # visited = [0 for i in range(n)]
        for i,node in enumerate(manager):
            if node != -1:
                graph[node].append(i)
        
        def dfs(node):
            ans = 0
            
            for emp in graph[node]:
                temp = dfs(emp) + informTime[node]
                # print(temp)
                ans = max(temp,ans)
            return ans

        # print(graph)

        # for i in range(n):
        return dfs(headID)