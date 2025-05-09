# Problem: Lexicographically Smallest Equivalent String - https://leetcode.com/problems/lexicographically-smallest-equivalent-string/

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        
        parent = [ i for i in range(26)]
        # size = [1 for _ in range(26)]

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]] 
                x = parent[x]
            return x

        def union(x, y):
            x_ = find(x)
            y_ = find(y)
            if x_ != y_:
                # if size[x_] < size[y_]:
                    # x_, y_ = y_, x_
                if y_ < x_:
                    parent[x_] = y_
                else:
                    parent[y_] = x_
                # size[x_]+= size[y_]
        

        for i in range(len(s1)):
            val1 = ord(s1[i]) - 97
            val2 = ord(s2[i]) - 97

            if val1 <= val2:
                union(val1,val2)
            else:
                union(val2,val1)
        
        ans = ["" for _ in range(len(baseStr))]
        for l in baseStr:
            temp = ord(l) - 97
            val = find(temp)

            ans.append(chr(val + 97))
        
        # print(parent)
        return "".join(ans)
