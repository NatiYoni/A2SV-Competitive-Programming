# Problem: Sorting the Sentence - https://leetcode.com/problems/sorting-the-sentence/

class Solution:
    def sortSentence(self, s: str) -> str:
        arr = [""] * 9
        s = s.split(" ")
        # print(s)

        for i in range(len(s)):
            arr[int(s[i][-1]) - 1] = s[i][:-1]
        
        return " ".join(arr).strip()