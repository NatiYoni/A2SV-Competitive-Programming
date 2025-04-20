# Problem: Evaluate Division - https://leetcode.com/problems/evaluate-division/

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        graph = defaultdict(list)

        for i, (a,b) in enumerate(equations):
            graph[a].append((b,values[i]))
            graph[b].append((a,1/values[i]))
        
        # print(graph)
        ans = [-1 for _ in range(len(queries))]

        for i, (a,b) in enumerate(queries):
        
            if (a in graph) and (b in graph):

                if a == b:
                    ans[i] = 1
                    continue

                dq = deque([(a,1)])
                # print(dq)
                # temp = 1
                visited = set()
                # parent = []
                # val = []

                while dq:
                    # for _ in range(len(dq)):
                    node, val = dq.popleft()
                    if node == b:
                        ans[i] = val
                        break
                    
                    for neigh, neigh_val in graph[node]:
                        if neigh not in visited:
                            visited.add(node)
                            dq.append((neigh,neigh_val * val))


        return ans