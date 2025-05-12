# Problem: Circumference of a Tree - https://codeforces.com/gym/102694/problem/A

import sys, collections, math, random, bisect

input = lambda: sys.stdin.readline().strip()

inp = lambda: int(input())
inlt = lambda: list(map(int, input().split()))
insr = lambda: list(input())
invr = lambda: map(int, input().split())

def dd(type_func=int):
    return collections.defaultdict(type_func)

def is_in_bounds(grid, i, j):
    return 0 <= i < len(grid) and 0 <= j < len(grid[0])

directions = [(-1,0),(0,1),(0,-1),(1,0),(1,1),(-1,-1),(-1,1),(1,-1)]

rand_no = random.randint(1, 1000000000)

def solve():
    n = inp()
    
    graph = collections.defaultdict(list)
    for _ in range(n-1):
        x,y = invr()
        graph[x - 1].append(y - 1)
        graph[y - 1].append(x - 1)

    visited = [0 for i in range(n)]
    dq = collections.deque()

    dq.append(0)
    count = 0
    idx = -1
    while dq:
        count += 1 
        for _ in range(len(dq)):
            # print(dq)
            node = dq.popleft()
            visited[node] = 1
            for neigh in graph[node]:
                if visited[neigh] != 1:
                    
                    dq.append(neigh)
                    idx = neigh    
                    
         
    

    visited = [0 for i in range(n)]
    dq = collections.deque()

    dq.append(idx)
    count = -1
    ans = 0
    while dq:
        count += 1 
        for _ in range(len(dq)):
            # print(dq)
            node = dq.popleft()
            visited[node] = 1
            for neigh in graph[node]:
                if visited[neigh] != 1:
                    
                    dq.append(neigh)

        ans = max(ans,count)
    print(ans * 3)


    pass

def main():
    multi = False  # Set to True for multi-test cases
    t = inp() if multi else 1
    for _ in range(t):
        solve()

if __name__ == '__main__':
    main()