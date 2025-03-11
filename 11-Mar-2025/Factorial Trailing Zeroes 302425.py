# Problem: Factorial Trailing Zeroes - https://leetcode.com/problems/factorial-trailing-zeroes/

class Solution:
    def trailingZeroes(self, n: int) -> int:
        def recursive(n):
            if n == 0:
                return 1

            return n * recursive(n - 1)
        
        val = recursive(n)
        count = 0
     
        
        while val % 10 == 0:
            count += 1
            
            val = val // 10
        
        return count

        
            

       