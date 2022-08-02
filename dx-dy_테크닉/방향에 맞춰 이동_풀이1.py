N = int(input())

# 동서남북, 입력에 맞는 이동 좌표
dxdy = {
    'N' : (0, 1),
    'E' : (1, 0),
    'S' : (0, -1),
    'W' : (-1, 0)
}
x, y = 0, 0

for _ in range(N):
    direction, cnt = input().split()
    cnt = int(cnt)
    
    # 이동 횟수만큼 좌표 갱신
    for _ in range(cnt):
        x, y = x + dxdy[direction][0], y + dxdy[direction][1]

print(x, y)
