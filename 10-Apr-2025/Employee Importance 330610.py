# Problem: Employee Importance - https://leetcode.com/problems/employee-importance/

"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
            
            graph = defaultdict(list)
            visited = set()
            
            for emp in employees:
                graph[emp.id].append(emp.importance)
                graph[emp.id].append(emp.subordinates) 
            
            # print(graph)
            # ans = 0
            
            def dfs(graph,visited,id,ans):
                visited.add(id)
                ans = graph[id][0]
                for sub in graph[id][1]:
                    if sub not in visited:
                        ans += dfs(graph,visited,sub,ans)
                        #ans  += graph[sub][0]
                    # print(ans,graph[sub][0])

                return ans
            return dfs(graph,visited,id,0)

                 