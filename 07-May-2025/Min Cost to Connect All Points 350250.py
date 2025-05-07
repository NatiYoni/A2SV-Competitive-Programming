# Problem: Min Cost to Connect All Points - https://leetcode.com/problems/min-cost-to-connect-all-points/

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        arr = []
        parent = {}
        size = defaultdict(int)
        ans = [0]

        for i in range(len(points)):
            x = tuple(points[i])
            parent[x] = x
            size[x] = 1
            for j in range(i+1,len(points)):
                diff = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                arr.append((points[i],points[j],diff))


        arr.sort(key = lambda x:x[2])
        
        def find(x):
            while x != parent[x] :
                parent[x] = parent[parent[x]]

                x = parent[x] 
            
            return x
        
        def union(x,y,c):
            x_ = find(x)
            y_ = find(y)

            if x_ != y_:
                if size[x_] < size[y_]:
                    x_, y_ = y_, x_
                parent[y_] = x_
                size[x_] += size[y_]
                ans[0] += c
        

        for x,y,w in arr:
            union(tuple(x),tuple(y),w)

        return ans[0]