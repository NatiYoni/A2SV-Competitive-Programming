# Problem: Shifting Letters II - https://leetcode.com/problems/shifting-letters-ii/description/

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        shift_effect = [0] * (n + 1)

        for start,end,k in shifts:
            if k == 1:
                shift_effect[start] += 1
                shift_effect[end + 1] -= 1
            else:
                shift_effect[start] -= 1
                shift_effect[end + 1] += 1
        
        

        result = []
        shift = 0
        for i in range(n):
            shift += shift_effect[i] 
            result.append(chr((ord(s[i]) - ord('a') + shift) % 26 + ord('a')))

        return ''.join(result)
            
                