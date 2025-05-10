# Problem: Removing Stars From a String - https://leetcode.com/problems/removing-stars-from-a-string/description/

class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for ch in s:
            if stack and ch =="*":
                stack.pop()
                continue 
            stack.append(ch)
        return "".join(stack)