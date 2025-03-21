# Problem: C - Compare T-Shirt Sizes - https://codeforces.com/gym/585107/problem/C

from collections import Counter
 
t = int(input())
result = []
 
for i in range(t):
    a, b = input().split()
    count_a = Counter(a)
    count_b = Counter(b)
 
    if a[-1] == b[-1]:
        if count_a == count_b:
            result.append("=")
        elif (count_a["X"] > count_b["X"] and a[-1] == "L") or (count_a["X"] < count_b["X"] and a[-1] == "S"):
            result.append(">")
        elif (count_a["X"] > count_b["X"] and a[-1] == "S") or (count_a["X"] < count_b["X"] and a[-1] == "L"):
            result.append("<")
 
    else:
        if a[-1] == "L" or b[-1] == "S":
            result.append(">")
        elif a[-1] == "S" or b[-1] == "L":
            result.append("<")
 
for size in result:
    print(size)
 