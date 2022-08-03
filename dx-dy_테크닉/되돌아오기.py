n = int(input())

mapper = {
    'N' : 0,
    'S' : 1,
    'W' : 2,
    'E' : 3
}

dxs, dys = [0, 0, -1, 1], [1, -1, 0, 0]

x, y = 0, 0
ans = 0
back = False
for _ in range(n):
    direction, dist = input().split()
    dist = int(dist)

    for _ in range(dist):
        x, y = x + dxs[mapper[direction]], y + dys[mapper[direction]]
        ans += 1
        if (x == 0) and (y == 0):
            back = True
            break
    
    if back:
        break

if back:
    print(ans)

else:
    print(-1)
