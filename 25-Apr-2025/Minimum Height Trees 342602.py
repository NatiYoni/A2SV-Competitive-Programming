# Problem: Minimum Height Trees - https://leetcode.com/problems/minimum-height-trees/

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        graph = defaultdict(list)
        degree = [0 for _ in range(n)]

        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
            degree[a] += 1
            degree[b] += 1

        # print(graph,degree)
        min_ = math.inf
        ans = []
        dq = deque()

        for i, val in enumerate(degree):
            if val <= 1 :
                dq.append(i)
                degree[i] -= 1
                
        # print(dq)
        ans = []
        while dq:
            ans = list(dq)
            for _ in range(len(dq)):
                node = dq.popleft() 
                
                for neigh in graph[node]:
                    degree[neigh] -= 1
                    
                    if degree[neigh] == 1:
                        dq.append(neigh)
        
                    # print(degree)
        return ans































        # for i in range(n):
        #     visited = [0 for _ in range(n)]
        #     dq = deque()

        #     dq.append(i)
        #     h = 0
            
        #     while dq:
                
        #         for _ in range(len(dq)):
        #             node = dq.popleft()
        #             visited[node] = 1

        #             for neigh in graph[node]:
                        
        #                 if visited[neigh] == 0 :
        #                     dq.append(neigh)
        #         h += 1
            
        #     if h == min_:
        #         ans.append(i)
                
        #     elif h < min_:
        #         ans.clear()
        #         ans.append(i)
        #         min_ = h
            
            
            # print(ans)

  
        # return ans
 