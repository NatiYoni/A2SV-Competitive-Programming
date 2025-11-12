# Problem: Number of Laser Beams in a Bank - https://leetcode.com/problems/number-of-laser-beams-in-a-bank/

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        pre = 0 
        ans = 0
        n = len(bank)
        for val in bank:
            cnt = val.count("1")
            ans += pre * cnt 
            if cnt:
                pre = cnt
        
        return ans

            
