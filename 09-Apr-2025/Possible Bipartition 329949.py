# Problem: Possible Bipartition - https://leetcode.com/problems/possible-bipartition/

class Solution:

    def dfs(self,graph,node,visited):
        temp = True

        for num in graph[node]:
            # print(visited,num)
            if visited[num] == -1:
                if visited[node] == 0:
                    visited[num] = 1
                else:
                    visited[num] = 0
                
                temp = temp and self.dfs(graph,num,visited)
            elif visited[num] == visited[node]:
                return False
        
        return temp



    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        
        graph = defaultdict(list)

        for a,b in dislikes:
            graph[a - 1].append(b -1)
            graph[b - 1].append(a - 1)
        
        print(graph)

        visited = [-1]*n 
        result = True

        for i in range(n):
            if visited[i] == -1:
                visited[i] = 1

                result = result and self.dfs(graph, i, visited)
        
        return result



       

            