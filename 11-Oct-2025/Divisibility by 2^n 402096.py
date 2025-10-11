# Problem: Divisibility by 2^n - https://codeforces.com/contest/1744/problem/D

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


    if n == 1:
        print(0 if arr[0] % 2 == 0 else -1)
        return
    
    upper = 2 ** n
    cnt = 0

    for val in arr:
        while val % 2 == 0:
            val //= 2
            cnt += 1
    
    # print(cnt)
    need = n - cnt
    if need <= 0:
        print(0)
        return

    ava = []
    for val in range(1,n+1):
        cnt = 0
        while val % 2 == 0:
            val //= 2
            cnt += 1
        if cnt > 0:
            ava.append(cnt)

    # print(need, ava)
    ava.sort(reverse = True)
    ans = 0
    for val in ava:
        ans += 1
        need -= val
        if need <= 0:
            print(ans)
            return
    
    print(-1)



            



    
    


    pass

def main():
    multi = True  # Set to True for multi-test cases
    t = inp() if multi else 1
    for _ in range(t):
        solve()
        

if __name__ == '__main__':
    main()