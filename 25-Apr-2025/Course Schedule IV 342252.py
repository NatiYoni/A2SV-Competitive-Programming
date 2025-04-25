# Problem: Course Schedule IV - https://leetcode.com/problems/course-schedule-iv/description/

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        graph = defaultdict(list)
        degree = [0 for _ in range(numCourses)]

        for a,b in prerequisites:
            graph[a].append(b)
            degree[b] += 1

        dq = deque()
        for i,val in enumerate(degree):
            if val == 0:
                dq.append(i)  
        
        res = defaultdict(set)
        while dq:
            for _ in range(len(dq)):
                node = dq.popleft()

                for neigh in graph[node]:
                    degree[neigh] -= 1
                    res[neigh].add(node)
                    res[neigh].update(res[node])

                    if degree[neigh] == 0:
                        dq.append(neigh)


        # print(res)
        # print(graph)
        ans = [False for i in range(len(queries))]
        for i, (a,b) in enumerate(queries):
            ans[i] = a in res[b]
        
        return ans
