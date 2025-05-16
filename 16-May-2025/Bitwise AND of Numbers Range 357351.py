# Problem: Bitwise AND of Numbers Range - https://leetcode.com/problems/bitwise-and-of-numbers-range/

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        len1 = left.bit_length()
        len2 = right.bit_length()


        if len1 != len2:
            return 0
        
        val = left & right
        xor_ = left ^ right
        temp = xor_.bit_length()

        return val & -1 << temp
        


















        # val1 = 0
        # i = 0
        # temp = -1
        # while i < (val.bit_length()):
        #     if val & (val1 << i) == 0:
        #         temp = i
        #     i += 1
        # print(temp)
        # i = 0
        # while i < temp - 1:
        #     val &= (1 << i)
        #     i += 1
        
        # return val
        # print(temp)
