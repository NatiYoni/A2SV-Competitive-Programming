# Problem: Count the Number of Consistent Strings - https://leetcode.com/problems/count-the-number-of-consistent-strings/

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        
        ans = 0
        seen = set()
        for word in allowed:
            seen.add(word)
        
        for word in words:
            flag = True
            for w in word:
                if w not in seen:
                    flag = False
                    break
                
            if flag:
                ans += 1
            
        return ans


