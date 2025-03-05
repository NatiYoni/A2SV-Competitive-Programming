# Problem: Rabbits in Forest - https://leetcode.com/problems/rabbits-in-forest/

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        
        # answers.sort()

        
        # total = 0
        # for i in range(1,len(answers)):
        #     if answers[i-1] == 0:
        #         total += 1
        #         print(total)
        #     elif answers[i] != answers[i-1]:
        #         total = answers[i-1] + 1
        
        # total += answers[-1] + 1
        
        # print(total)
        # return total

        counter = Counter(answers)
        total = 0

        for key, val in counter.items():
            if key + 1 >= val:
                total += key + 1
            else:
                total += (key + 1) * math.ceil(val / (key + 1))
        
        return total


