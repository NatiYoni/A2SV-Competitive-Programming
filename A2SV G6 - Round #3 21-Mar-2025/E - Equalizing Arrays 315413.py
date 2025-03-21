# Problem: E - Equalizing Arrays - https://codeforces.com/gym/588468/problem/E

import sys, collections, math, random

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
    arr1 = inlt()
    m = inp()
    arr2 = inlt()

    left = right = 0
    count = 0
    sum1 = 0
    sum2 = 0

    while left < n and right < m:
        # if sum1 == 0 and sum2 == 0
        if  left < n and right < m and sum1 == sum2:

            sum1 += arr1[left]
            sum2 += arr2[right]

            count += 1
            left += 1
            right += 1
            

        elif right < m and sum1 > sum2:
            sum2 += arr2[right]
            right += 1
            


        else :
            sum1 += arr1[left]
            left += 1
    
    while left < n:
        sum1 += arr1[left]
        left += 1
    
    while right < m:
        sum2 += arr2[right]
        right += 1
 
    if sum1 == sum2:
        print(count)
    else:
        print(-1)

    pass

def main():
    multi = False  # Set to True for multi-test cases
    t = inp() if multi else 1
    for _ in range(t):
        solve()

if __name__ == '__main__':
    main()