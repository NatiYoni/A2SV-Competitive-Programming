# Problem: Count Good Numbers - https://leetcode.com/problems/count-good-numbers/

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = (10**(9) + 7)
        if n % 2 == 0:
           ans =  pow(5, (n//2),mod) * pow(4, (n//2),mod)
        else:
            ans = pow(5,math.ceil(n/2),mod) * pow(4,(n//2),mod)

        return ans % mod