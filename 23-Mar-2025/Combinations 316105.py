# Problem: Combinations - https://leetcode.com/problems/combinations/

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        arr = []
        def bk(i, temp):
            
            if len(temp) == k:
                arr.append(temp.copy())
                return 
            
            if i > n:  
                return
            
            temp.append(i)
            bk(i+1,temp)
            temp.pop()

            bk(i+1,temp)


        bk(1,[])
        return arr