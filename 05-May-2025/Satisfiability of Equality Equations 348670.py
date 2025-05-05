# Problem: Satisfiability of Equality Equations - https://leetcode.com/problems/satisfiability-of-equality-equations/

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent = [i for i in range(26)]
        size = [1] * 26
        
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]] 
                x = parent[x]
            return x
        
        def union(x, y):
            x_ = find(x)
            y_ = find(y)
            if x_ != y_:
                if size[0] < size[0]:
                    x_, y_ = y_, x_
                parent[y_] = x_
        
        for a,b,c,d in equations:
            if b == "=":
                
                num1 = ord(a) - 97
                num2 = ord(d) - 97
                # print(num1,num2)
                union(num1,num2)
            

        
        for a,b,c,d in equations:
            num1 = ord(a) - 97
            num2 = ord(d) - 97
            
            val1 = find(num1)
            val2 = find(num2)

            if  val1 == val2 and b == "!":
                return False

            elif val1 != val2 and b == "=":
                return False
        
        return True


                