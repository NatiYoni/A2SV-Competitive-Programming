# Problem: Happy Number - https://leetcode.com/problems/happy-number/description/

class Solution:
    def isHappy(self, n: int) -> bool:
        slow = n
        fast = n
        while True:
            slow = sum(int(digit) ** 2 for digit in str(slow))
            fast = sum(int(digit) ** 2 for digit in str(fast))
            fast = sum(int(digit) ** 2 for digit in str(fast))
            
            if fast == 1:
                return True  
            if slow == fast:
                return False  
            
            