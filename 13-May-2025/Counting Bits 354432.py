# Problem: Counting Bits - https://leetcode.com/problems/counting-bits/

class Solution:
    def countBits(self, n: int) -> List[int]:
        
        if n == 0:
            return [0]
        
        # print(bin(100000))
        temp = 1
        ans = []
        for i in range(n+1):
            val = str(bin(i))
            ans.append(val.count("1"))
        
        return ans

