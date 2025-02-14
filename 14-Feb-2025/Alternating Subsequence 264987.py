# Problem: Alternating Subsequence - https://codeforces.com/contest/1343/problem/C

from collections import defaultdict

t = int(input())
output = []
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))

    left = right = 0
    temp = []
    max_num = float("-inf")

    for right in range(n):

        if arr[right] < 0:
            max_num = max(max_num, arr[right])
            
            if right < n-1  and arr[right+1] > 0 or right == n -1:
                temp.append(max_num)
                max_num = 0
        else:
            max_num = max(max_num, arr[right])
             
            if right < n-1  and arr[right+1] < 0 or right == n -1:
                temp.append(max_num)
                max_num = float("-inf")
    
    output.append(sum(temp))
for sum in output:
    print(sum)

