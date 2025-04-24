# Problem: Find Eventual Safe States - https://leetcode.com/problems/find-eventual-safe-states/

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)

        degree = [0 for _ in range(n)]
        dq = deque()

        ans =[]
        path = defaultdict(list)
        for i,neighs in enumerate(graph):
            
            # if len(neighs) == 0:
            #     ans.append(i)

            for neigh in neighs:
                path[neigh].append(i)
                degree[i] += 1
        
        # print(path,degree)

        for i,val in enumerate(degree):
            if val == 0:
                dq.append(i)

        # print(dq,degree)
        
        while dq:
            for _ in range(len(dq)):
                node = dq.popleft()
                ans.append(node)

                for neigh in path[node]:
                    degree[neigh] -= 1

                    if degree[neigh] == 0:
                        dq.append(neigh)

        ans.sort()
        return ans

