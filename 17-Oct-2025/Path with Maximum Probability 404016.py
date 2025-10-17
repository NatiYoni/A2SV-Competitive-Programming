# Problem: Path with Maximum Probability - https://leetcode.com/problems/path-with-maximum-probability/

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)
        for i in range(len(edges)):
            u,v = edges[i]
            w = succProb[i]
            graph[u].append((v,w))
            graph[v].append((u,w))
        
        heap = [(-1,start_node)]
        visited = [0] * n
        while heap:
            w, u = heappop(heap)
            if u == end_node:
                return abs(w)

            visited[u] = 1
            for neigh,weigh in graph[u]:
                if not visited[neigh]:
                    heappush(heap,(weigh * w, neigh))


        return 0