# Problem: Percentage of Letter in String - https://leetcode.com/problems/percentage-of-letter-in-string/description/%20meaning/

class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        counter = Counter(s)

        ans = floor(counter[letter] / len(s) * 100)
        return ans