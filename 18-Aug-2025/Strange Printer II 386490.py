# Problem: Strange Printer II - https://leetcode.com/problems/strange-printer-ii/

class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        n = len(targetGrid)
        m = len(targetGrid[0])
        

        top = defaultdict(int)
        down = defaultdict(int)
        left = defaultdict(int)
        right = defaultdict(int)

        for i in range(n):
            for j in range(m):
                val = targetGrid[i][j]
                if val not in top:
                    top[val] = i
                    down[val] = i
                    left[val] = j
                    right[val] = j
                else:
                    down[val] = max(i,down[val]) 
                    left[val] = min(j,left[val])
                    right[val] = max(j,right[val])

        
        arr = list(top.keys())
        graph = defaultdict(list)
        degree = [0] * 61
        
        # print(arr)
        for i in range(len(arr)):
            node = arr[i]
            tp = top[node]
            dn = down[node]
            lt = left[node]
            rt = right[node]

            seen = set()
            for j in range(tp,dn+1):
                for k in range(lt,rt+1):
                    
                    if targetGrid[j][k] != node:
                        seen.add(targetGrid[j][k])
            
            for neigh in seen:
                degree[node] += 1
                graph[neigh].append(node)
        
        dq = deque([i for i in range(60+1) if degree[i] == 0])
        # print(dq)
        while dq:
            node = dq.popleft()

            for neigh in graph[node]:
                # print(node,neigh)
                degree[neigh] -= 1
                if degree[neigh] == 0:
                    dq.append(neigh)
        

        
        return sum(degree) == 0

                   
        


