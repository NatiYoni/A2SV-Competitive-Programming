# Problem: Maximize the Number of Target Nodes After Connecting Trees II - https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-ii/

class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        graph1 = defaultdict(list)
        graph2 = defaultdict(list)

        for a,b in edges1:
            graph1[a].append(b)
            graph1[b].append(a)
        
        
        for a,b in edges2:
            graph2[a].append(b)
            graph2[b].append(a)
        
        # graph1
        g21 = g22 = 0
        lvl = 0
        dq = deque()
        dq.append(0)
        visited = [0] * len(graph2)
        while dq:
            for i in range(len(dq)):
                node = dq.popleft()
                visited[node] = 1
                if lvl % 2 == 0:
                    g21 += 1
                else:
                    g22 += 1
                
                for neigh in graph2[node]:
                    if visited[neigh] == 0:
                        dq.append(neigh)

            lvl += 1
        
        mx = max(g21,g22)
        # print((g21,g22))

        # graph1
        n = len(graph1)
        ans = [0] * n
        g11 = g12 = 0
        dq.append(0)
        lvl = 0
        while dq:

            for i in range(len(dq)):
                if lvl % 2 == 0:
                    g11 += 1
                else:
                    g12 += 1

                node = dq.popleft()
                ans[node] = 2 if lvl % 2 else 1

                for neigh in graph1[node]:
                    if ans[neigh] == 0:
                        dq.append(neigh)

            lvl += 1
        
        for i,val in enumerate(ans):
            if val == 1:
                ans[i] = mx + g11
            else:
                ans[i] = mx + g12
        
        return ans
        

        


