# Problem: All Ancestors of A Node in Directed Acyclic Graph - https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        graph = defaultdict(list)
        for x,y in edges:
            graph[y].append(x)

        output = [[] for i in range(n)]
        visited = [0 for i in range(n)]
        # print(output)

        memo = defaultdict()
        def dfs(node):
            if node in memo:
                return memo[node]

            ans = set()

            for parent in graph[node]:
                ans.add(parent)
                
                ans.update(dfs(parent))
                
            memo[node] = ans
            # print(memo)
            print(ans)
            return ans

        for i in range(n):
            output[i].extend(sorted(dfs(i)))
        
        return output