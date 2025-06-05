# Problem: Team - https://codeforces.com/contest/231/problem/A

n = int(input())
count = 0

for _ in range(n):
    p, v, t = map(int, input().split())

    if p + v + t >= 2:
        count += 1

print(count)