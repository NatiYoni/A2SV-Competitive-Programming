# Problem: Remove Letter To Equalize Frequency - https://leetcode.com/problems/remove-letter-to-equalize-frequency/

class Solution:
    def equalFrequency(self, word: str) -> bool:
        word_counter = Counter(word)
        frequency_counter = Counter(word_counter.values())

        if len(frequency_counter) == 1 and 1 in frequency_counter:
            
            return True
        if len(frequency_counter) == 1 and len(word_counter) == 1:
            return True
        
        elif len(frequency_counter) == 2:
            frequency = list(frequency_counter.keys())

            if 1 in frequency_counter and frequency_counter[1] == 1:
                return True

            if abs(frequency[0] - frequency[1]) == 1 and frequency_counter[max(frequency)] == 1:
                return True
  
        
        return False


