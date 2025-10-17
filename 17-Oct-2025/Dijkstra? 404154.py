# Problem: Dijkstra? - https://codeforces.com/problemset/problem/20/C

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

import heapq
def dijkstra(n, graph, src):
    dist = [float('inf')] * n
    dist[src] = 0
    pq = [(0, src)]
    parent = [i for i in range(n)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]: continue
        for v, w in graph[u]:
            if dist[v] > d + w:
                dist[v] = d + w
                parent[v] = u
                heapq.heappush(pq, (dist[v], v))
    return dist,parent
def solve():
    graph = dd(list)

    n,m = invr()
    
    for _ in range(m):
        u,v,w = invr()
        graph[u].append((v,w))
        graph[v].append((u,w))
    
    dst,parent = dijkstra(n+1, graph, 1)
    # print(dst,parent)

    val = n
    ans = []

    while val != 1:
        if parent[val] == val:
            print(-1)
            return
        
        ans.append(val)
        val = parent[val]

    print(1,*reversed(ans))
    pass

def main():
    multi = False  # Set to True for multi-test cases
    t = inp() if multi else 1
    for _ in range(t):
        solve()

if __name__ == '__main__':
    main()