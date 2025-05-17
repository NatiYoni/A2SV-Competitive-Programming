# Problem: Decode XORed Array - https://leetcode.com/problems/decode-xored-array/description/

class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        
        ans = []
        ans.append(first)

        for val in encoded:
            ans.append(ans[-1] ^ val)
        
        return ans
