def in_range(x, y, n):
    return 0 <= x and x < n and 0 <= y and y < n

N, M = map(int, input().split())

arr = [
    [0] * N
    for _ in range(N)
]

dxs, dys = [0, 0, -1, 1], [-1, 1, 0, 0]

result = []
for _ in range(M):
    r, c = map(int, input().split())
    # 색칠 진행, 리스트는 0부터 idx 시작
    x, y = r - 1, c - 1
    arr[x][y] = 1

    # 편안한 격자
    comf = 0
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy

        if in_range(nx, ny, N) and arr[nx][ny] == 1:
            comf += 1
    
    if comf == 3:
        result.append(1)
    
    else:
        result.append(0)

for i in result:
    print(i)
