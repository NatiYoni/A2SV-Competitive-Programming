# Problem: Minimum Cost to Convert String I - https://leetcode.com/problems/minimum-cost-to-convert-string-i/description/?envType=problem-list-v2&envId=shortest-path

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        def floyd(n, edges):
            dist = [[float('inf')] * n for _ in range(n)]
            for i in range(n):
                dist[i][i] = 0
            for u, v, w in edges:
                dist[u][v] = min(dist[u][v], w)

            for k in range(n):
                for i in range(n):
                    for j in range(n):
                        if dist[i][k] + dist[k][j] < dist[i][j]:
                            dist[i][j] = dist[i][k] + dist[k][j]


            return dist
        
        graph = []
        for i in range(len(original)):
            u = ord(original[i]) - 97
            v = ord(changed[i]) - 97
            w = cost[i]
            graph.append([u,v,w])
        

        dist = floyd(26,graph)

        ans = 0
        for i in range(len(source)):
            u = ord(source[i]) -97
            v = ord(target[i]) - 97
            ans += dist[u][v]

        return ans if ans != math.inf else -1