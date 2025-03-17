# Problem: Decode String - https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
        
        def decode(s):
           
            if not s:
                return ""

            if s[0].isnumeric():
                
                i = 0
                while i < len(s) and s[i].isdigit():
                    i += 1

                num = int(s[:i])


                count, j = 1, i + 1
                while count > 0:
                    if s[j] == "[":
                        count += 1
                    elif s[j] == "]":
                        count -= 1
                    
                    j += 1

                
                substring = decode(s[i + 1: j - 1])

                return num * substring + decode(s[j:])
            else:
                return s[0] + self.decodeString(s[1:])

                          

        return decode(s)
        