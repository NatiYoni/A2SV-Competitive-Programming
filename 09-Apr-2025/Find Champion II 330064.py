# Problem: Find Champion II - https://leetcode.com/problems/find-champion-ii/

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:

        graph = defaultdict(list)

        for a, b in edges:
            graph[a].append(b)
        
        # print(graph,visited)


        def dfs(node):
            visited[node] = 1
            nonlocal count
            for num in graph[node]:
                if visited[num] == -1:
                    count += 1
                    dfs(num)
                
            
            return count


        for i in range(n):
            visited = [-1 for _ in range(n)]
            count = 0
            dfs(i)
            # print(count)
            if count == n - 1:
                return i
            
            count = 0

        
        return -1

        pass