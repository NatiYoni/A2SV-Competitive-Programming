# Problem: Most Stones Removed with Same Row or Column - https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        
        size = {}  
        parent = {}

        for val in stones:
            parent[tuple(val)] = tuple(val)
            size[tuple(val)] = 1

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]] 
                x = parent[x]
            return x

        def union(x, y):
            x_ = find(x)
            y_ = find(y)
            if x_ != y_:
                if size[x_]< size[y_]:
                    x_, y_ = y_, x_
                parent[y_] = x_
                size[x_]+= size[y_]
        
        for i in range(len(stones)):
            for j in range(i,len(stones)):
                if stones[i][0] ==  stones[j][0] or  stones[i ][1] ==  stones[j][1]:
                    union(tuple(stones[i]),tuple(stones[j]))
        
        ans = 0
        for key,val in parent.items():
            if key == val:
                ans += 1
        print(parent)
        return len(stones) - ans