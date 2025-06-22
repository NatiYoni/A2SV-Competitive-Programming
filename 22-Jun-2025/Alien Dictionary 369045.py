# Problem: Alien Dictionary - https://practice.geeksforgeeks.org/problems/alien-dictionary/1

from collections import defaultdict,deque

class Solution:
    def findOrder(words):
        # code here
        n = len(words)
        graph = defaultdict(list)
        degree = defaultdict(int)
        
        temp = words[0]
        for i in range(1,n):
            l = 0
            
            while l < len(temp) and l < len(words[i]) and temp[l] == words[i][l]:
                l += 1
            
            
            
            if l < len(temp) and l < len(words[i]): 
                graph[temp[l]].append(words[i][l])
                
                degree[temp[l]] += 0
                degree[words[i][l]] += 1
            elif len(temp) > len(words[i]):
                return ""
                
            temp = words[i]
        
        for i in range(n):
            for l in words[i]:
                degree[l] += 0
                
            
        dq = deque()    
        for i,val in degree.items():
            if val == 0:
                dq.append(i)
        
        ans = []
        while dq:
            node = dq.popleft()
            ans.append(node)
            
            
            for neigh in graph[node]:
                degree[neigh] -= 1
                
                if degree[neigh] == 0:
                    dq.append(neigh)
        
        for i in degree:
            if degree[i] != 0:
                return ""

        
        
        return ans
        
        
      