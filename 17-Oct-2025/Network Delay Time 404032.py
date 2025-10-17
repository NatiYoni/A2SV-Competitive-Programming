# Problem: Network Delay Time - https://leetcode.com/problems/network-delay-time/description/

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        for u,v,w  in times:
            graph[u].append((v,w))
        
        visited = [0] * (n + 1)
        heap = [(0,k)]
        visited[0] = 1
        ans = 0
        while heap:
            w, node = heappop(heap)
            
            if not visited[node]:
                ans = w
            visited[node] = 1

            for neigh,weigh in graph[node]:
                if not visited[neigh]: 
                    heappush(heap, ( w + weigh, neigh))
                   
        
        for val in visited:
            if not val:
                return -1
        
        return ans