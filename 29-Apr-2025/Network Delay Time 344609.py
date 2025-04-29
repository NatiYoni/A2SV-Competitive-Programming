# Problem: Network Delay Time - https://leetcode.com/problems/network-delay-time/

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        graph = defaultdict(list)
        for u,v,d in times:
            graph[u - 1].append((v - 1,d))
        
        

        res = [math.inf for _ in range(n)]
        res[k - 1] = 0

        dq = deque()
        dq.append(k - 1)
        
        while dq:
            for _ in range(len(dq)):
                node = dq.popleft()

                for neigh,val in graph[node]:
                    if (val + res[node]) < res[neigh]:
                        res[neigh] = val + res[node]
                        dq.append(neigh) 
        
        ans = max(res)
        # print(res)
        if ans == math.inf:
            return -1
        else:
            return ans

                