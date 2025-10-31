# Problem: Number of Ways to Reach a Position After Exactly k Steps - https://leetcode.com/problems/number-of-ways-to-reach-a-position-after-exactly-k-steps/

class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        Mod = 10**9 + 7

        diff = abs(endPos - startPos)

        if diff % 2 != k % 2 or diff > k:
            return 0
        
        r =  (k + diff) // 2
       
        return comb(k,r) % Mod