# Problem: D - Bomb Detection Validation - https://codeforces.com/gym/586960/problem/D

rows,cols = map(int, input().split())
 
def inBound(row,col):
    return 0 <= row < rows and 0 <= col < cols
 
mat = []
for i in range(rows):
    lst = list(input())
    mat.append(lst)
 
directions = [(-1,0),(0,1),(0,-1),(1,0),(1,1),(-1,-1),(-1,1),(1,-1)]
flag = False
 
for row in range(rows):
    for  col in range(cols):
 
        if mat[row][col] == "*":
            continue
 
        count = 0
        for a,b in directions:
            new_row = row + a
            new_col = col + b
            
            if  inBound(new_row,new_col) and mat[new_row][new_col] == "*":
                count += 1
 
        if  count != 0 and mat[row][col] == ".": 
            flag = True
            
 
        elif mat[row][col].isdigit() and count != int(mat[row][col]):
            flag = True
    if flag:
        break
if flag:
    print("NO")
else:
    print("YES")