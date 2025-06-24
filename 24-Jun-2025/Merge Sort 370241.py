# Problem: Merge Sort - https://codeforces.com/problemset/problem/873/D

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
    # length = n.bit_length()
    # cnt = n.bit_count()
    # temp = int("1" * length,2) 

    # if cnt != length:
    #     temp += 2 if n % 2 == 1 else 0
    # else:
    #     temp = int("1" * (length + 1),2) - 2
    

    if m % 2 == 0: 
        print(-1)
        return 

    arr = []
    for i in range(n):
        arr.append(i+1)

    cnt_arr = [1]
    def divCon(arr):
        if cnt_arr[0] > m:
            return []
        
        if len(arr) == 1:
            return arr
        
        if m == cnt_arr[0] :
            return arr
        cnt_arr[0] += 2
        mid = (len(arr) + 1)//2
        left = divCon(arr[:mid])
        right = divCon(arr[mid:])

        return right + left
        
    ans = divCon(arr)
    if (len(ans) == len(arr) and cnt_arr[0] == m):    print(*ans )
    else: print(-1)
    

    pass

def main():
    multi = False  # Set to True for multi-test cases
    t = inp() if multi else 1
    for _ in range(t):
        solve()

if __name__ == '__main__':
    main()



