# Problem: Is Subsequence - https://leetcode.com/problems/is-subsequence/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # s_c =  Counter(s)
        # t_c = Counter(t)

        # count = 0
        # for a in s_c:
        #     if a in t_c and s_c[a] <= t_c[a]:
        #         count += 1
        
        # return count == len(s_c)
        r = 0
        l = 0
        while l < len(s) and r < len(t):
            if s[l] == t[r]:
                l += 1
            
            r += 1
        
        return  l == len(s)