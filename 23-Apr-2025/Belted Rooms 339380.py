# Problem: Belted Rooms - https://codeforces.com/problemset/problem/1428/B

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
    s = insr()
    # graph = dd(list)

    # for i in range(n):
    #     if i < n - 1:
    #         if s[i] =="-":
    #             graph[i].append(i+1)
    #             graph[i+1].append(i)
    #         elif s[i] == ">":
    #             graph[i].append(i+1)
    #         else:
    #             graph[i+1].append(i)
        
    #     else:
    #         if s[i] =="-":
    #             graph[0].append(i)
    #             graph[i].append(0)
    #         elif s[i] == ">":
    #             graph[i].append(0)
    #         else:
    #             graph[0].append(i)
    
    ans = 0
    cw = ccw = 0

    # print(s)
    for i in range(len(s)):
        if s[i] == "-" or s[(i+1)%n]=="-":
            ans += 1   

        if s[i] == ">":
            cw += 1
        elif s[i] == "<":
            ccw += 1
        
    # print(ccw,cw)
    # if cw == 0:
    #     ans += ccw
    # elif ccw == 0:
    #     ans += cw
    
    if cw == 0 or ccw == 0:
        print(n)
        return
    
    print(ans)


    
    pass

def main():
    multi = True # Set to True for multi-test cases
    t = inp() if multi else 1
    for _ in range(t):
        solve()

if __name__ == '__main__':
    main()


  




