# Problem: The Two Routes - https://codeforces.com/problemset/problem/601/A

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
    n,m = invr()
    
    graph = dd(list)
    train = False
    for i in range(m):
        a,b = invr()
        graph[a].append(b)
        graph[b].append(a)

        if (a ==1 and b == n) or (a == n and b ==1):
            train = True
    
    road = dd(list)
    if train:
        for i in range(1,n+1):
            for j in range(i+1,n+1):
                if j not in graph[i]:
                    road[i].append(j)
                    road[j].append(i)

    # print(train)

    dq = collections.deque()
    dq.append(1)
    visited = [0] * (n+1)
    visited[1] = 1
    ans = 0
    while dq:
        ans += 1
        for i in range(len(dq)):
            node = dq.popleft()
            if train:
                for neigh in road[node]:
                    if neigh == n:
                        print(max(1,ans))
                        return
                    if  visited[neigh] == 0:
                        dq.append(neigh)
                        visited[neigh] = 1
            else:
                for neigh in graph[node]:
                    if neigh == n:
                        print(max(1,ans))
                        return
                    if  visited[neigh] == 0:
                        dq.append(neigh)
                        visited[neigh] = 1
    print(-1)
                    
    pass

def main():
    multi = False  # Set to True for multi-test cases
    t = inp() if multi else 1
    for _ in range(t):
        solve()

if __name__ == '__main__':
    main()