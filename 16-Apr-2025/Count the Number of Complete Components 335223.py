# Problem: Count the Number of Complete Components - https://leetcode.com/problems/count-the-number-of-complete-components/

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        
        graph = defaultdict(list)

        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)

        visited = [0 for i in range(n)]
        
        # print(graph)

        
        def dfs(node):
            cur_connected = []
            # flag = False
            cur_connected.append(node)
            visited[node] = 1
            # temp = len(graph[node])
            
            
            for neigh in graph[node]:
                if visited[neigh] == 0:

                    cur_connected.extend(dfs(neigh))
                    # print(len(graph[node]),edge,node)
                    # if len(graph[neigh]) != edge or flag:
                        
                        # print(node,neigh)
                        # print(len(graph[node]),edge)
                        # temp = 0
                        # flag = True
            # print(flag,node) 
            # print(cur_connected)
            return cur_connected
        
        ans = 0
        for i in range(n):
            if visited[i] == 0:
                # print(dfs(i))
                # print(i)
                # edge = len(graph[i])
                cur_connected  = dfs(i)
                for cur in cur_connected:
                    if len(graph[cur]) >= len(cur_connected) - 1:
                        flag = True
                    else:
                        flag = False
                        break
                
                if flag:
                    ans += 1
    
        
        return ans