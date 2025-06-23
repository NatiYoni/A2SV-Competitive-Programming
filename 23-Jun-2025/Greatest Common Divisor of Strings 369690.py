# Problem: Greatest Common Divisor of Strings - https://leetcode.com/problems/greatest-common-divisor-of-strings/

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        l = 0
        count = Counter(str1)
        count2 = Counter(str2)

        if str1 + str2 != str2 + str1:
            return ""
        
        length = gcd(len(str1), len(str2))
        return str1[:length]