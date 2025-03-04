# Problem: Maximum Odd Binary Number - https://leetcode.com/problems/maximum-odd-binary-number/

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        counter = Counter(s)
        return (counter["1"] - 1 ) *  "1" + counter["0"] * "0" + "1"