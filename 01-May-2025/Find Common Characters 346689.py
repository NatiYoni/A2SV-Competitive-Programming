# Problem: Find Common Characters - https://leetcode.com/problems/find-common-characters/

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        min_ = Counter(words[0])
        for word in words[1:]:
            min_ &= Counter(word) 
        res = []
        for char, freq in min_.items():
            res.extend([char] * freq)
            
        return res
                
