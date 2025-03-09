# Problem: Split a String in Balanced Strings - https://leetcode.com/problems/split-a-string-in-balanced-strings/

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        
        count_r = 0
        count_l = 0
        count = 0

        for i in range(len(s)):
            if s[i] == "L":
                count_l += 1
            else:
                count_r += 1
            
            if count_l == count_r:
                count += 1
            
        return count