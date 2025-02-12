# Problem: Partition Labels - https://leetcode.com/problems/partition-labels/

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        s_counter = Counter(s)
        save = set()
        count = 0
        output = []

        for letter in s:
            count += 1
            s_counter[letter] -= 1

            if s_counter[letter] == 0:
                save.discard(letter)  
            else:
                save.add(letter)
            
            if  not save and count > 0:
                output.append(count)
                count = 0
        
        return output
        

