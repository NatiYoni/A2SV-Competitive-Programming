# Problem: Check if One String Swap Can Make Strings Equal - https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/description/

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        counter1 = Counter(s1)
        counter2 = Counter(s2)

        if counter2 == counter1:
            r = 0
            val = 0
            while r < len(s2):
                if s1[r] != s2[r]:
                    val += 1
                
                r += 1
            
            if val > 2:
                return False
            else:
                return True
        else:
            return False