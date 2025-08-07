# Problem: Minimum Number of Pushes to Type Word II - https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/

class Solution:
    def minimumPushes(self, word: str) -> int:
        cnt = Counter(word)

        cnter = sorted(cnt.items(), key = lambda  x : x[1], reverse = True)
        print(cnter)
        ans = 0
        i = 1
        for i, (key, val) in enumerate(cnter):
            ans += (i//8 + 1) * val
        
        return ans