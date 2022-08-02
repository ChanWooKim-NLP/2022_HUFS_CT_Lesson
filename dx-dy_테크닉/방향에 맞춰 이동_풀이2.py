N = int(input())

# 최초 좌표
x, y = 0, 0

# 방향에 따른 이동
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

# 입력값에 따라 dx, dy값 달라짐
dxdy = {'N' : 3, 'E' : 0, 'S' : 1, 'W' : 2}

for _ in range(N):
    direction, cnt = input().split()
    cnt = int(cnt)
    
    # 이동 방향 따라 이동 좌표 갱신
    dir = dxdy[direction]
    
    # cnt만큼 특정 방향으로 이동
    x += dx[dir] * cnt
    y += dy[dir] * cnt
    

print(x, y)
