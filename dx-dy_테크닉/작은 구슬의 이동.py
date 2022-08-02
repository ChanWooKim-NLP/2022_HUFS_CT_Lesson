def in_range(x, y, n):
    return 1 <= x and x <= n and 1 <= y and y <= n

n, t = map(int, input().split())
r, c, d = input().split()

x, y = int(r), int(c)

mapper = {
    'R' : 0,
    'D' : 1,
    'U' : 2,
    'L' : 3
}

dxs, dys = [0, 1, -1, 0], [1, 0, 0, -1]

dir_num = mapper[d]

for _ in range(t):
    nx, ny = x + dxs[dir_num], y + dys[dir_num]

    # 벽에 부딫히거나 / 움직이거나
    # t번 반복. 굳이 복잡하게 
    if in_range(nx, ny, n):
        x, y = nx, ny
    
    else:
        dir_num = 3 - dir_num

print(x, y)

'''
# 시간초과 풀이
while t != 0:
    nx, ny = x + dxs[dir_num], y + dys[dir_num]

    if not in_range(nx, ny, n):
        dir_num = 3 - dir_num # 반대 방향 회전
        t -= 1

    x, y = x + dxs[dir_num], y + dys[dir_num]
    t -= 1

print(x, y)
'''
