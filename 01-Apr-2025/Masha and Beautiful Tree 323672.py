# Problem: Masha and Beautiful Tree - https://codeforces.com/problemset/problem/1741/D

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
    arr = inlt()


    # if n == 1:
    #     print(0)
    #     return

    count = 0
    def sort(l,r):
        nonlocal count

        ans = []
        # print(l,r)
        if len(l) == 1 and len(r) == 1:
            if l[0] < r[0]:
                ans.append(l[0])
                ans.append(r[0])
            else:
                ans.append(r[0])
                ans.append(l[0])
                count += 1
        
        else:
            if l[0] < r[0]:
                ans.extend((l + r))
            else:
                ans.extend((r + l))
                count += 1

        # print(ans)
        return ans
        pass

    def divide(arr):
        if len(arr) == 1:
            return arr
        
        mid = len(arr) // 2

        l = divide(arr[:mid])
        r = divide(arr[mid:])
        
        # print(l,r)
        return sort(l,r)

    
    res = divide(arr)
    # print(res)

    for i in range(1,n):
        if res[i] < res[i - 1]:
            print(-1)
            return
    
    print(count)
    pass

def main():
    multi = True
    t = inp() if multi else 1
    for _ in range(t):
        solve()

if __name__ == '__main__':
    main()