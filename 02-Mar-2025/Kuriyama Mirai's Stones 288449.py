# Problem: Kuriyama Mirai's Stones - https://codeforces.com/contest/433/problem/B

import sys
import collections
input = sys.stdin.readline

def inp():
    return int(input())
def inlt():
    return list(map(int, input().split()))
def invr():
    return map(int, input().split())


def solve():
    n = inp()
    arr = inlt()
    m = inp()

    sorted_arr = sorted(arr)

    for i in range(1,n):
        sorted_arr[i] += sorted_arr[i-1] 
        arr[i] += arr[i-1]
    
    for i in range(m):
        type, l, r = invr()
        if type == 1:
            if l - 1 != 0: 
                print(arr[r - 1] - arr[l - 2])
            else:
                print(arr[r - 1])
        else:
            if l - 1 != 0: 
                print(sorted_arr[r - 1] - sorted_arr[l - 2])
            else:
                print(sorted_arr[r - 1])
            

def main():
    multi = False # if multiple Test cases change it to true
    t = int(input()) if multi else 1
    for _ in range(t):
        solve()

if __name__ == '__main__':
    main()