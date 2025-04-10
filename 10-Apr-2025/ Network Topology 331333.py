# Problem:  Network Topology - https://codeforces.com/problemset/problem/292/B

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
    node, q = invr()
    graph = dd(list)
    for i in range(q):
        a, b = invr()
        graph[a].append(b)
        graph[b].append(a)
    
    # print(graph)

    bus = True
    star = True
    ring = True
    count2 = 0
    count1 = 0
    count3 = 0
    for val in graph.values():
        n = len(val)
        # print(val)
        if n == 1:
            count1 += 1
        if n == 2:
            count2 += 1
        if n > 2:
            count3 += 1
    # print(count1,count2,count3)
    if count3 == 0 and count2 == node - 2 and count1 == 2:
        print("bus topology")
    
    elif count3 == 1  and count2 == 0 and count1 == node - 1:
        print("star topology")
    
    elif count3 == 0 and count2 == node and count1 == 0:
        print("ring topology")
    else:
        print("unknown topology")

            
        


        
    pass

def main():
    multi = False  # Set to True for multi-test cases
    t = inp() if multi else 1
    for _ in range(t):
        solve()

if __name__ == '__main__':
    main()