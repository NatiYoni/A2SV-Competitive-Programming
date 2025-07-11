# Problem: Isomorphic Strings - https://leetcode.com/problems/isomorphic-strings/

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hash1 = {}
        hash2 = {}
        for i,l in enumerate(s):
            if (l not in hash1 and t[i] in hash2) or (l in hash1 and t[i] not in hash2):
                return False
            
            elif (l in hash1 and t[i] in hash2) and (hash1[l] != t[i] or hash2[t[i]] != l):
                return False


            else:
                hash1[l] = t[i]
                hash2[t[i]] = l
        
        return True
