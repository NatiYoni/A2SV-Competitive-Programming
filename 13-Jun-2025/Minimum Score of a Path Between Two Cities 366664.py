# Problem: Minimum Score of a Path Between Two Cities - https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/description/

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        
        parent = [i for i in range(n)]
        meta = [[1,math.inf] for i in range(n)]

        def find(x):

            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            
            return x



        def union(x,y,v):
            xp = find(x)
            yp = find(y)

            if meta[xp][0] < meta[yp][0]:
                xp , yp = yp, xp

            if xp != yp:
                parent[yp] = xp
                meta[xp][0] += meta[yp][0]

            meta[xp][1] = min(meta[xp][1],v,meta[yp][1]) 


        for a,b,c in roads:
            union(a - 1, b - 1,c)
        

        ans = find(0)


        return meta[ans][1]


        
