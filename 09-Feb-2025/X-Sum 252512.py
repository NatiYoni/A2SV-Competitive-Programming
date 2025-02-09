# Problem: X-Sum - https://codeforces.com/problemset/problem/1676/D

from collections import defaultdict
t = int(input())
output = []

for i in range(t):
    m , n = map(int, input().split())
    mat = []
    
    for num in range(m):
        arr = list(map(int, input().split()))
        mat.append(arr)

    primary = defaultdict(int)
    secondary = defaultdict(int)
    max_num = 0
    for i in range(m):
        for j in range(n):
            primary[(i-j)] += mat[i][j] 
            secondary[(i+j)] += mat[i][j]
    
    for i in range(m):
        for j in range(n):
            max_num = max(max_num, primary[(i-j)] + secondary[(i+j)] - mat[i][j])

    output.append(max_num)
    
for num in output:
    print(num)

