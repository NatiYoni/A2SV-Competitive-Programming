# Problem: Sort Characters By Frequency - https://leetcode.com/problems/sort-characters-by-frequency/description/

class Solution:
    def frequencySort(self, s: str) -> str:
        frequency = Counter(s)
        sorted_frequency = dict(sorted(frequency.items(),key = lambda x: x[1], reverse = True))

        output = []
        for key, value in sorted_frequency.items():
            output.append(key * value)
        
        return "".join(output)
            
