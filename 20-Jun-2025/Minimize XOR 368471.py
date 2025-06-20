# Problem: Minimize XOR - https://leetcode.com/problems/minimize-xor/description/

class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        cnt = 0
        while num2 > 0:
            if num2 & 1:
                cnt += 1
            
            num2 >>= 1
        
        x = num1.bit_count()
        if cnt == x:
            return num1

        elif cnt > x:
            rem = cnt - x
            l = 0
            while rem:
                if not( num1 & (1 << l)):
                    num1 |= 1 << l
                    rem -= 1
                l += 1

            return num1 
        
        i = num1.bit_length()
        bit = ["0"] * i
        while cnt:
            if num1 & (1 << i):
                bit[i] = "1"
                cnt -= 1

            i -= 1
            
        
        ans = "".join(reversed(bit))

        return int(ans,2)
        
        
        
       