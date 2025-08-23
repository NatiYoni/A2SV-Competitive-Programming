# Problem: Largest Color Value in a Directed Graph - https://leetcode.com/problems/largest-color-value-in-a-directed-graph/

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)

        graph = defaultdict(list)
        deg = [0] * n

        for a,b in edges:
            graph[b].append(a)
            deg[a] += 1
        
        dq = deque()
        for i,val in enumerate(deg):
            if val == 0:
                dq.append(i)
                

        dp = [[0]*26 for i in range(n)]
        while dq:
            node = dq.popleft()
            cl = ord(colors[node]) - ord("a")
            dp[node][cl] += 1
            for neigh in graph[node]:
                for i in range(26):
                    dp[neigh][i] = max(dp[node][i],dp[neigh][i])

                deg[neigh] -= 1
                if deg[neigh] == 0: 
                    dq.append(neigh)

                    
            
            
        
        for val in deg:
            if val != 0:
                return -1

        # print(dp)
        return max(max(color) for color in dp)

        


            