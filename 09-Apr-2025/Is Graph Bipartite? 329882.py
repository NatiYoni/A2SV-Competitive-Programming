# Problem: Is Graph Bipartite? - https://leetcode.com/problems/is-graph-bipartite/

class Solution:
    def dfs(self, graph, node,color):
        temp = True
        for neighbour in graph[node]:
            # print(color)
            if color[neighbour] == -1:
                if color[node] == 0:
                    color[neighbour] = 1
                else:
                    color[neighbour] = 0

                temp = temp and self.dfs(graph,neighbour,color)

            elif color[neighbour] == color[node]:
                return False
            
        
        return temp
            
        pass

    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [-1 for _ in range(n)]
        # print(color)
        result = True

        for node in range(n):
            if color[node] == -1:
                color[node] = 0

                result = result and self.dfs(graph,node,color)
        
        return result



