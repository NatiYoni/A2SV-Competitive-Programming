# Problem: Vowels of All Substrings - https://leetcode.com/problems/vowels-of-all-substrings/

class Solution:
    def countVowels(self, word: str) -> int:
        vowel = {"a","o","u","e","i"}
        ans = 0
        for i, l in enumerate(word):
            if l in vowel:
                ans += (i+1) * (len(word)-i)
        
        return ans