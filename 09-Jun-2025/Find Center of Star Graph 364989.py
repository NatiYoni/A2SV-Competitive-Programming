# Problem: Find Center of Star Graph - https://leetcode.com/problems/find-center-of-star-graph/

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        graph = defaultdict(list)

        for a,b in edges:
            graph[a-1].append(b-1)
            graph[b-1].append(a-1)
        
        visited = [0 for _ in range(len(edges) + 1)]

        dq = deque()
        dq.append(0)
        temp = 0
        while dq:
            node = dq.popleft()

            visited[node] = 1
            for neigh in graph[node]:
                if visited[neigh] == 0:
                    dq.append(neigh)
            
            temp = node
        
        # print(temp)


        return graph[temp][0] + 1