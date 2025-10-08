# Problem: Count Primes - https://leetcode.com/problems/count-primes/

class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0

        primes = [True] * (n)
        primes[0] = False
        primes[1] = False
        i = 2
        while i < n:

            if primes[i]:
                cnt = 2
                while cnt * i < n:
                    idx = i * cnt
                    primes[idx] = False 
                    cnt += 1

            i += 1
        ans = 0
        for val in primes:
            if val:
                ans += 1
        return ans

