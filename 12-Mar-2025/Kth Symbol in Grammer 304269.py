# Problem: Kth Symbol in Grammer - https://leetcode.com/problems/k-th-symbol-in-grammar/

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:

        flag = False

        def kTh(n,k,flag):
            if k == 1:
                return (k, flag)
            
            if k == 2:
                return (k, flag)
            
            
            if k > (2 ** (n -  1)) // 2:
                
                if flag:
                    flag = False

                else:
                    flag = True

                k = ((2 ** (n - 1))// 2) - abs((2 ** (n-1) ) - k)
                
                print(k)
                
            
            return kTh(n-1, k,flag)

        

        k, flag = kTh(n,k,flag)
        print(k,flag)

        if k == 1:
            if flag == False:
                return 0
            else:
                return 1
        else:
            if flag == False:
                return 1
            else:
                return 0

        # def kth(n,k):
        #     if n == 1:
        #         return 0
            
        #     num = (2 ** (n -  1)) // 2
        #     if k >  num:
        #         return 1 - kth(n-1,k - num)
        
        #     return kth(n-1,k)
        
        # return kth(n,k)