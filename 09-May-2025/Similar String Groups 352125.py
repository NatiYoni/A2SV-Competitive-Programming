# Problem: Similar String Groups - https://leetcode.com/problems/similar-string-groups/

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        
        if len(strs) <= 1 or len(strs[0]) <= 3:
            return 1

        parent = {strs[i]:strs[i] for i in range(len(strs))}
        size = { strs[i]: 1 for i in range(len(strs))}

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

                size[x_]+= size[y_]
                parent[x_] = y_
        
        def violate(x,y):
            diff = 0
            for i in range(len(strs[0])):
                if strs[x][i] != strs[y][i] :
                    diff += 1
                
                if diff > 2:
                    return True
            
            if diff == 2 or diff == 0:
                return False
            
            return True



        diff = 0
        for i in range(len(strs)):
            for j in range(i,len(strs)):

                if  not violate(i,j):
                    union(strs[i],strs[j])
        ans = set()
        for val in parent:
            ans.add(find(val))
        
        return len(ans)

