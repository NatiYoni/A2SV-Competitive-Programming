# Problem: Separate Black and white balls - https://leetcode.com/problems/separate-black-and-white-balls/

class Solution:
    def minimumSteps(self, s: str) -> int:
        
        counter = 0  
        answer = 0   

        for right in range(len(s) - 1, -1, -1):
            if s[right] == '0':
                counter += 1  
            else:
                answer += counter  
        
        return answer
            