# Problem: Longest Nice Substring - https://leetcode.com/problems/longest-nice-substring/

class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        
        seen = set(s)

        for i, c in enumerate(s):
            if c.swapcase() not in seen:
                left = self.longestNiceSubstring(s[:i]) 
                right = self.longestNiceSubstring(s[i+1:])

                return left if len(left) >= len(right) else right

        return s