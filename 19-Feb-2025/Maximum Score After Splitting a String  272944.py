# Problem: Maximum Score After Splitting a String  - https://leetcode.com/problems/maximum-score-after-splitting-a-string/

class Solution:
    def maxScore(self, s: str) -> int:

        prefix = [0] * len(s)
        prefix[0] = int(s[0])

        for i in range(1,len(s)):
            prefix[i] = prefix[i-1] + int(s[i]) 
        
        suffix = 0
        max_num = 0
        for i in range(len(prefix)-1):
            
            if prefix[i] == 0:
                suffix += 1
            
            elif i > 0 and prefix[i] == prefix[i-1]:
                suffix +=  1

            max_num = max(max_num, (suffix + prefix[-1] - prefix[i]))
        
        return max_num

        
