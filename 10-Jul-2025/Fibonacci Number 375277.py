# Problem: Fibonacci Number - https://leetcode.com/problems/fibonacci-number/

class Solution:
    def fib(self, n: int) -> int:
        memo = {}
        def fibo(n):
            if n == 1:
                return 1
            elif n == 0:
                return 0
            
            if n in memo:
                return memo[n]
            
            val = fibo(n-1) + fibo(n-2)
            memo[n] = val
            return val
        
        return fibo(n)