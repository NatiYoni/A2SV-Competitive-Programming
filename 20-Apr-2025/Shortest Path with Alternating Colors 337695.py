# Problem: Shortest Path with Alternating Colors - https://leetcode.com/problems/shortest-path-with-alternating-colors/description/

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:

        v_r = [0 for _ in range(n) ]
        v_b = [0 for _ in range(n) ]
        ans = [-1 for _ in range(n) ]
        ans[0] = 0 
        v_r[0] = v_b[0] = - 1
        graph = defaultdict(list)
        

        for a,b in redEdges:
            graph[a].append((b,"r"))
        
        for a,b in blueEdges:
            graph[a].append((b,"b"))
        
        # print(graph)
        dq = deque([(0,False)])
        # pre_col = deque()
        # pre_col.append(0)
        count = 0
        

        while dq:
            count += 1
            # print(count)
            # pre = pre_col.popleft()
            for i in range(len(dq)):
                node ,pre = dq.popleft()
                # print(node)
                for neigh, col in graph[node]:
                     
                    # if pre != col and (v_r[neigh] == 0 or v_b[neigh] == 0):
                    #     # print(v_r,v_b)
                    #     if ans[neigh] == -1:
                    #         ans[neigh] = count
                    #     # print(graph[node])
                    #     dq.append((neigh,col))
                    #     # pre_col.append(col)

                        
                    #     v_r[neigh] = -1
                        
                    #     v_b[neigh] = -1
                    
                    if pre != col:

                        if col == "r" and v_r[neigh] == 0:
                            v_r[neigh] = -1
                            dq.append((neigh, col))
                            
                            if ans[neigh] == -1:
                                ans[neigh] = count

                        elif col == "b" and v_b[neigh] == 0:
                            v_b[neigh] = -1
                            dq.append((neigh, col))

                            if ans[neigh] == -1:
                                ans[neigh] = count


        # print(v_r,v_b)
        return ans