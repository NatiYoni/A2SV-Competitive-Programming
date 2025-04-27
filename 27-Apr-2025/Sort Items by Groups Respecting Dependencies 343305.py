# Problem: Sort Items by Groups Respecting Dependencies - https://leetcode.com/problems/sort-items-by-groups-respecting-dependencies/

class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
  
        for i,val in enumerate(group):
            if val == -1:
                group[i] = m
                m += 1


        item_graph = defaultdict(list)
        group_graph = defaultdict(set)
        item_degree = [0 for _ in range(n)]
        group_degree = [0 for _ in range(m)]

        for i,vals in enumerate(beforeItems):
            item_degree[i] = len(vals)

            for val in vals:
               
                item_graph[val].append(i)
                
                gr1,gr2 = group[val],group[i]

                if gr1 != gr2 :
                    if gr2 not in group_graph[gr1]:
                        group_graph[gr1].add(gr2)
                        group_degree[gr2]  += 1


        # print(item_degree,group_degree)

       
        def bfs(graph,degree):

            dq = deque()
            for i,val in enumerate(degree):
                if val == 0:
                    dq.append(i)
                    
            ans = []
            while dq:
                for _ in range(len(dq)):
                    node = dq.popleft()
                    ans.append(node)

                    for neigh in graph[node]:
                        degree[neigh] -= 1

                        if degree[neigh] == 0:
                            dq.append(neigh)
            return ans
                
        
        item_sort = bfs(item_graph,item_degree[:])
        group_sort = bfs(group_graph,group_degree[:])
        # print(group_degree)
        # print(item_sort,group_sort)

        if len(item_sort) != n or len(group_sort) != m:
            return []


        g_s = defaultdict(list)
        for node in item_sort:
            g = group[node]
            g_s[g].append(node)
        

        ans = []
        for g in group_sort:
            ans.extend(g_s[g])
        
        return ans










        # graph = defaultdict(list)
        # groups = defaultdict(list)
        # degree = [0 for _ in range(n)]
        # d_g = [0 for _ in range(m)]

        # seen = set()
        # for i,vals in enumerate(beforeItems):
        #     for val in vals:
        #         graph[val].append(i)
        #         if group[i] != -1 and group[i] != group[val]  and ((i,val) not in seen):
        #             seen.add((i,val))
        #             seen.add((val,i))
        #             d_g[group[i]] += 1

        #         if  ((i,val) not in seen):
        #             degree[i] = len(vals)
            
        
        # print(d_g)
        # dq = deque()
        # for i,val in enumerate(degree):
        #     if val == 0 and d_g[group[i]] == 0:
        #         dq.append(i)
        #     # else:


        # print(dq)
        # temp = []
        # while dq:
        #     for _ in range(len(dq)):
        #         node = dq.popleft()
                
        #         if group[node] != -1:
        #             groups[group[node]].append(node)
        #             temp.append("g"+str(group[node]))
        #         else:
        #             temp.append(node)

        #         for neigh in graph[node]:
        #             degree[neigh] -= 1

        #             if degree[neigh] == 0:
        #                 dq.append(neigh)
        
        # print(temp,groups,degree)
        # for val in degree:
        #     if val != 0:
        #         return []
        
        # ans = []
        
        # gr = [0 for i in range(m)]
        # for g in temp:
        #     if str(g).isdigit():
        #         ans.append(g)
        #     elif (gr[int(g[1:])] == 0):
        #         gr[int(g[1:])] = 1
        #         for val in groups[int(g[1:])]:
        #             ans.append(val)
            

   

        # return ans


            

                

