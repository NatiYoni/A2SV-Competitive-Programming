# Problem: First Unique Character in a String - https://leetcode.com/problems/first-unique-character-in-a-string/description/?envType=problem-list-v2&envId=queue

class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        hash = {}
        for i,l in enumerate(s):
            if l in hash:
                hash[l][1] += 1 
            else:
                hash[l] = [i,1]

        for key,(i,val) in hash.items():
            if val == 1:
                return i
        
        return -1