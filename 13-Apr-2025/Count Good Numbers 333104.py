# Problem: Count Good Numbers - https://leetcode.com/problems/count-good-numbers/

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        # mod = (10**(9) + 7)
        # if n % 2 == 0:
        #    ans =  pow(5, (n//2),mod) * pow(4, (n//2),mod)
        # else:
        #     ans = pow(5,math.ceil(n/2),mod) * pow(4,(n//2),mod)

        # return ans % mod

        mod = (10**(9) + 7)

        def pow(x,n):
            res = 1
            while n > 0:
                if n % 2:
                    res = (res * x)

                n = n // 2
                x = (x*x) % mod
            
            return res

        even = ceil(n/2)
        odd = n//2

        return pow(5,even) * pow(4,odd) % mod