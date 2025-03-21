# Problem: Generate Binary Strings Without Adjacent Zeros - https://leetcode.com/problems/generate-binary-strings-without-adjacent-zeros/description/

class Solution:
    def validStrings(self, n: int) -> List[str]:
        arr = []

        def valid(temp):

            if len(temp) == n:
                arr.append("".join(temp))
                return 

            # print(arr)
            for i in ("0","1"):

                if temp and temp[-1] == "0" and i == "0":
                    continue
                    
                temp.append(i)
                valid(temp)
                temp.pop()

                
                
        valid([])
        return arr