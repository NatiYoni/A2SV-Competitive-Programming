# Problem: Letter Case Permutation - https://leetcode.com/problems/letter-case-permutation/

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        
        ans = set()
        for i in range(2**len(s)):
            arr = []
            k = 0
            
            while k < len(s):
                temp = i
                temp &= (1 << k)
                # print(i,k,temp)
                if  s[k].isalpha():
                    if temp > 0:
                        arr.append(s[k].upper())
                    else:
                        arr.append(s[k].lower()) 
                else:
                    arr.append(s[k])


                k += 1

            ans.add("".join(arr))
            # print(arr)
        
        return list(ans)
