# Problem: Find Kth Bit in Nth Binary String - https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

class Solution:

   
    def findKthBit(self, n: int, k: int) -> str:

        flag = False
        def kthBit(n,k,flag):

            if n == 1:
                return "0" if not flag else "1"
            
            temp = 2 ** (n - 1) 
            
            if temp == k :

                return "1" if not flag else "0"

            elif k < temp:
                return kthBit(n-1 , k, flag)

            if temp < k :
                new = temp * 2 - k
                return  kthBit(n - 1, new, not flag) 

            


        return kthBit(n, k, flag)