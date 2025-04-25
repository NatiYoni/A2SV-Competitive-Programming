# Problem: Course Schedule II - https://leetcode.com/problems/course-schedule-ii/description/

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)
        degree = defaultdict(int)

        for a,b in  prerequisites:
            graph[b].append(a)
            degree[a] += 1
        
        dq = deque()
    
        for i in range(numCourses):
            if degree[i] == 0:
                dq.append(i)

        ans = []
        while dq:
            # print(dq)
            cur = dq.popleft()
            ans.append(cur)

            for neigh in graph[cur]:
                degree[neigh] -= 1 

                if degree[neigh] == 0:
                    dq.append(neigh)

        if len(ans) == numCourses:
            return ans
        
        # print(ans)
        return []

      

        