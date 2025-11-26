# Problem: Decode Ways - https://leetcode.com/problems/decode-ways/

class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if n == 0 or s[0] == "0":
            return 0
        
        dp = [0] * (n)
        dp[0] = 1

        for i in range(1,n):

            if s[i] != "0":
                dp[i] = dp[i-1]
            
            val = int(s[i-1:i+1])
            if 10 <= val <= 26:
                if i == 1:
                    dp[i] += 1
                else:
                    dp[i] += dp[i-2]
        
        return dp[-1]

        