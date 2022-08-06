def in_range(x, y, n):
    return 0 <= x and x < n and 0 <= y and y < n

N = int(input())

arr = [
    list(map(int, input().split()))
    for _ in range(N)
]

temp_arr = [
    [0] * N
    for _ in range(N)
    ]

r, c = map(int, input().split())

# 파이썬 형식에 맞추기 위해 x, y 선언
x, y = r-1, c-1

dxs, dys = [1, -1, 0, 0], [0, 0, -1, 1]
center = arr[x][y]

if center == 1:
    arr[x][y] = 0

elif center == 2:
    arr[x][y] = 0
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if in_range(nx, ny, N):
            arr[nx][ny] = 0
 
else:
    for dx, dy in zip(dxs, dys):
        for i in range(center):
            nx, ny = x + dx*i, y + dy*i
            if in_range(nx, ny, N):
                arr[nx][ny] = 0

# 중력에 의해 떨어짐
for col in range(N):
    temp_row = N-1
    for row in range(N-1, -1, -1):
        if arr[row][col] != 0:
            temp_arr[temp_row][col] = arr[row][col]
            temp_row -= 1

for i in range(len(temp_arr)):
    for j in temp_arr[i]:
        print(j, end=' ')
    print()
    
