def in_range(x, y, n, m):
    return 0 <= x and x < n and 0 <= y and y < m

n, m = map(int, input().split())

arr = [
    [0] * m
    for _ in range(n)
]

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
x, y = 0, 0
dir_num = 0

arr[x][y] = 1
for i in range(2, n*m + 1):
    nx, ny = x + dxs[dir_num], y + dys[dir_num]

    # 벽을 만났거나 이미 값이 채워져 있다면
    if not in_range(nx, ny, n, m) or arr[nx][ny] != 0:
        dir_num = (dir_num + 1) % 4
    
    x, y = x + dxs[dir_num], y + dys[dir_num]
    arr[x][y] = i

for i in range(n):
    for j in range(m):
        print(arr[i][j], end=' ')
    print()
