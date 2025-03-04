# Problem: Lemonade Change - https://leetcode.com/problems/lemonade-change/

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        # change = 0
        # count_5 = 0

        # for i, bill in enumerate(bills):

        #     if bill == 5:
        #         count_5 += 1
        #     else:
        #         count_5 -= 1
        #         if bill - change == 0 and i != len(bills) - 1:
        #             count_5 = 0
        #     print(count_5)
    
        #     if bill - change <= 5 and count_5 > 0 or count_5 == 0 and i == len(bills) - 1:
        #         change += 5
                
                
        #     else:
        #         return False

          
        #     print(change)
        # return True 

        count_5 = 0
        count_10 = 0

        for bill in bills:

            if bill == 5:
                count_5 += 1

            elif bill == 10:
                if count_5 == 0:
                    return False

                count_10 += 1
                count_5 -= 1

            else:
                if count_10 > 0 and count_5 > 0:
                    count_10 -= 1
                    count_5 -= 1
                
                elif count_5 >= 3:
                    count_5 -= 3
                
                else:
                    return False
        
        return True
 
                
