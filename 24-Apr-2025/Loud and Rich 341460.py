# Problem: Loud and Rich - https://leetcode.com/problems/loud-and-rich/description/

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)

        graph = defaultdict(list)
        degree = [0 for i in range(n)]

        for a,b in richer:
            graph[a].append(b)
            degree[b] += 1

        # print(graph,degree)
        dq = deque()
        ans = [-1 for i in range(n)]
        for i in range(n):
            if degree[i] == 0:
                dq.append((i,i))
                ans[i] = i




        top_order = []
        # print(dq)
        min_quiet = [i for i in range(n)]

        while dq:
            for i in range(len(dq)):
                node,min_ = dq.popleft()
                # top_order.append(node)
                ans[node] = min_

                for neigh in graph[node]:
                    degree[neigh] -= 1
                    
                    if quiet[min_] < quiet[min_quiet[neigh]]:
                        min_quiet[neigh] = min_

                    if degree[neigh] == 0:
                        dq.append((neigh,min_quiet[neigh]))

        # print(top_order)

        # ans = [-1 for i in range(n)]
        # for node in top_order:
        #     min_quiet = quiet[node]

        #     for neigh in graph[node]:
        #         min_quiet = neigh if quiet[neigh] < min_quiet else min_quiet
            
        #     ans[node] = min_quiet
        
        return ans
