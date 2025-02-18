# Problem: Minimum Processing Time - https://leetcode.com/problems/minimum-processing-time/

class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort(reverse = True)
        processorTime.sort()

        right = left = 0
        max_num = 0

        while right < len(tasks):  
            if right % 4 == 0 and right > 0:
                left += 1
            
            max_num = max(max_num, tasks[right] + processorTime[left])
            right += 1
        
        return max_num

