# Problem: Single Number III - https://leetcode.com/problems/single-number-iii/

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0

        for val in nums:
            xor ^= val

        bit = xor & -xor
        a = 0
        b = 0
        for val in nums:
            if bit & val:
                a ^= val
            else:
                b ^= val
        
        return  [a,b]
