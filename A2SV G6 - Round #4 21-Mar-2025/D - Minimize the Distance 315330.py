# Problem: D - Minimize the Distance - https://codeforces.com/gym/590053/problem/D

import sys
import collections
input = sys.stdin.readline
 
def inp():
    return int(input())
def inlt():
    return list(map(int, input().split()))
def insr():
    return list(input().strip())
def invr():
    return map(int, input().split())
 
 
def solve():
    n = inp()
    lst = inlt()
    lst.sort()
 
    if n % 2 == 0:
        print(lst[n//2 - 1])
    else:
        print(lst[n//2])
        
def main():
    multi = False # if multiple Test cases change it to true
    t = int(input()) if multi else 1
    for _ in range(t):
        solve()
 
if __name__ == '__main__':
    main()