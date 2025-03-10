# Problem: Segments with Small Spread - https://codeforces.com/edu/course/2/lesson/9/2/practice/contest/307093/problem/F

import sys
import collections
input = sys.stdin.readline


def inlt():
    return list(map(int, input().split()))
def invr():
    return map(int, input().split())



def solve():
    # solution here
    n, k = invr()
    arr = inlt ()

    q_max = collections.deque()
    q_min = collections.deque()
    res = 0

    # min_ =  float("inf")
    # max_ = float("-inf")
    
    l = 0
    for i in range(n):

        # if arr[i] < min_:
        #     min_ = arr[i]
        # if arr[i] > max_:
        #     max_ = arr[i]

        
        # if (max_ - min_) > k:
        #     l = len(q) - 1
        #     if arr[i] < min_:
        #         min_ = arr[i]
        #     if arr[i] > max_:
        #         max_ = arr[i]

        #     while l >= 0 and abs(arr[i] - q[l]) <= k: 
                
        #         min_ = min(q[l],min_)
        #         max_ = max(q[l],max_)
        #         l -= 1

        #     while l >= 0:
        #         q.popleft() 
        #         l -= 1              
        
        # q.append(arr[i])
        # res += len(q)
        

        while q_max and q_max[-1] < arr[i]:
            q_max.pop()

        while q_min and q_min[-1] > arr[i]:
            q_min.pop()
        
        q_min.append(arr[i])
        q_max.append(arr[i])

        while q_max and q_min and abs(q_max[0] - q_min[0]) > k:
            if q_max[0] == arr[l]:
                q_max.popleft()

            if q_min[0] == arr[l]:
                q_min.popleft()
            
            l += 1
        
        res += (i - l + 1)
        
    print(res)


def main():
    multi = False # if multiple Test cases change it to true
    t = int(input()) if multi else 1
    for _ in range(t):
        solve()

if __name__ == '__main__':
    main()