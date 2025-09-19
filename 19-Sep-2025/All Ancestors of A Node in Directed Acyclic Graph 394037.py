# Problem: All Ancestors of A Node in Directed Acyclic Graph - https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        parent = [set() for i in range(n)]

        graph = [[] for i in range(n)]
        deg = [0] * n

        for a,b in edges:
            graph[a].append(b)
            deg[b] += 1

        dq = deque([i for i in range(n) if deg[i] == 0])
        while dq:
            node = dq.popleft()

            for child in graph[node]:
                parent[child].update(parent[node])
                parent[child].add(node)
                # print(parent)
                deg[child] -= 1

                if deg[child] == 0:
                    dq.append(child)
        
        return [sorted(list(seen)) for seen in parent]
        

