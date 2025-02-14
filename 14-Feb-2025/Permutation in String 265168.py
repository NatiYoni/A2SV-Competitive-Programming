# Problem: Permutation in String - https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = len(s1)
        counter_s1 = Counter(s1)
        counter_s2 = {}

        left ,right = 0, 0

        while right < len(s2):

            if s2[right] not in counter_s2:
                counter_s2[s2[right]] = 0

            counter_s2[s2[right]] += 1 

            if right >= window:

                counter_s2[s2[left]] -= 1
                if counter_s2[s2[left]] == 0:
                    del counter_s2[s2[left]]
                left += 1

            if counter_s1 == counter_s2:
                return True
                
            right += 1
        
        return False
        