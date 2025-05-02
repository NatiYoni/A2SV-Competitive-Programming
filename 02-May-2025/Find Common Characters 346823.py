# Problem: Find Common Characters - https://leetcode.com/problems/find-common-characters/

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:

        count = Counter(words[0])
        
        for i in range(1,len(words)):
            count1 = Counter(words[i])

            for l in count:
                if l not in count1:
                    count[l] = 0
                elif count[l] > count1[l]:
                    count[l] = count1[l]
        
        ans = []
        for l in count:
            for _ in range(count[l]):
                ans.append(l)
        
        return ans
                

