# Problem: Find the City With the Smallest Number of Neighbors at a Threshold Distance - https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = defaultdict(list)
        for u,v,w in edges:
            graph[u].append((v,w))
            graph[v].append((u,w))

        city = [0] * n
        for i in range(n):
            visited = [0] * n

            heap = [(0,i)]
            cnt = -1
            while heap:
                cst, node = heappop(heap)
                if visited[node]: continue
                cnt += 1
                visited[node] = 1
                for neigh, w in graph[node]:
                    if not visited[neigh] and w + cst <= distanceThreshold:
                        heappush(heap, (w + cst,neigh))
                        
            
            city[i] = cnt   

        # print(city)
        mn = math.inf
        ans = 0
        for i in range(n-1,-1,-1):
            if city[i] < mn:
                ans = i
                mn = city[i]
        return ans