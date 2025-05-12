# Problem: Checking Existence of Edge Length Limited Paths - https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/

class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        edgeList.sort(key = lambda x:x[2])
        
        parent = [i for i in range(n)]
        size = [1 for i in range(n)]
        max_ = [0 for i in range(n)]
        
        for i,val in enumerate(queries):
            queries[i] = [i,val]

        queries.sort(key = lambda x:x[1][2])
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]] 
                x = parent[x]
            return x

        def union(x, y):
            x_ = find(x)
            y_ = find(y)
            
            if x_ != y_:
                if size[x_] < size[y_]:
                    x_, y_ = y_, x_
            
                parent[y_] = x_
                
                size[x_]+= size[y_]
                
        

        l = 0
        ans = [False] * len(queries)
        for idx,(x,y,w) in queries:
            while l < len(edgeList) and w > edgeList[l][2]:
                union(edgeList[l][0] ,edgeList[l][1])
                l += 1
            
            val1 = find(x) 
            val2 = find(y)

            if val1 == val2:
                ans[idx] = True
     
        
        # l = 0
        # for i,(x,y,w) in enumerate(queries):
        #     if w <= max_[0]:
        #         ans[i] = False
        #         continue
        #     val1 = find(x)
        #     val2 = find(y)  

        #     if val1 != val2:
        #         ans[i] = False
        
        return ans

