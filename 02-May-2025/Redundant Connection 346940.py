# Problem: Redundant Connection - https://leetcode.com/problems/redundant-connection/

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges))]
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]

            return parent[x]
        
        def union(x,y):
            x_ = find(x)
            y_ = find(y)
            

            if x_ != y_:
                parent[x_] = y_
        
        for edge in edges:
            a,b = edge
            a_ = find(parent[a  - 1])
            b_ = find(parent[b - 1])

            # print(a,b,a_,b_)
            if a_ == b_:
                return [a,b]
            else:
                union(a - 1,b - 1)