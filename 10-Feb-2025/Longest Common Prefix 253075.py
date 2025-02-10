# Problem: Longest Common Prefix - https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        result = strs[0]

        for string in strs[1:]:
            while string[:len(result)] != result:
                result = result[:-1]
                if not result:
                    return ""
    
        return result


