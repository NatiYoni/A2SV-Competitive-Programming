# Problem: Couse Schedule - https://leetcode.com/problems/course-schedule/

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = defaultdict(list) 
        degree = [0 for _ in range(numCourses)]

        for a, b in prerequisites:
            graph[b].append(a)
            degree[a] += 1

        
        dq = deque()
        for i,num in enumerate(degree):
            if num == 0:
                dq.append(i)
        
        while dq:
            for _ in range(len(dq)):
                node = dq.popleft()

                for neigh in graph[node]:
                    degree[neigh] -= 1

                    if degree[neigh] == 0:
                        dq.append(neigh)
        
        for i,val in enumerate(degree): 
            if val != 0:
                return False
        
        return True
        
