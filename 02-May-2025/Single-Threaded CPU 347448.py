# Problem: Single-Threaded CPU - https://leetcode.com/problems/single-threaded-cpu/

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:

        for i in range(len(tasks)):
            tasks[i].append(i)


        tasks.sort()
        cur_time = tasks[0][0]
        # print(tasks)
        ans = []
        arr = []

        i = 0
        while i < len(tasks) or arr:

            while i < len(tasks) and tasks[i][0] <= cur_time:
                heappush(arr,(tasks[i][1],tasks[i][2]))
                i += 1
            
            
            if arr:
                val = heappop(arr)
                ans.append(val[1])
                cur_time += val[0]
            else:
                cur_time = tasks[i][0]
            
        return ans