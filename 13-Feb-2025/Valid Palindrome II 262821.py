# Problem: Valid Palindrome II - https://leetcode.com/problems/valid-palindrome-ii/description/

class Solution:
    def validPalindrome(self, s: str) -> bool:

        left, right = 0, len(s) - 1
        delete_left = 1
        l_flag = True
        while (left < right) or (left == right and len(s) % 2 == 1):
            if s[left] != s[right] and delete_left == 1:
                left += 1
                delete_left -= 1
            elif s[left] != s[right] and delete_left < 1:
                l_flag = False
                break
            else:
                right -= 1
                left += 1
        
        left, right = 0, len(s) - 1
        delete_right = 1
        r_flag = True
        print(l_flag)

        while (left < right) or (left == right and len(s) % 2 == 1):
            if s[left] != s[right] and delete_right == 1:
                delete_right -= 1
                right -= 1
            elif s[left] != s[right] and delete_right < 1:
                r_flag = False
                break
            else:
                right -= 1
                left += 1
       
        return l_flag or r_flag

        

        # left, right = 0, len(s) - 1
        # d = 1
        # while (left < right) or (left == right and len(s) % 2 == 1):

        #     if s[left] != s[right] and d == 1:
        #         if s[left + 1] == s[right] and s[left] == s[right - 1]:
        #             if s[left + 1: left + 3] == s[right: right - 3:-1]:
        #                 left += 1
        #             else:
        #                 right -= 1


        #         elif s[left + 1] == s[right]:
        #             left += 1
        #         elif s[left] == s[right - 1]:
        #             right -= 1
        #         else:
        #             return False

        #         d = 0

        #     elif s[left] != s[right] and d < 1:
        #         return False
        #     else:
        #         right -= 1
        #         left += 1
        # return True
