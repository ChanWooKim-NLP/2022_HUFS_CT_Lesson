def in_range(x, y, n):
    return 0 <= x and x < n and 0 <= y and y < n

def move():
    global x, y

    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
    max_num = arr[x][y]
    track = [max_num]

    # 1회 이동
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy

        if in_range(nx, ny, n) and max_num < arr[nx][ny]:
            max_num = arr[nx][ny]
            x, y = nx, ny
            
            # boolean으로 이동 여부 판단
            return True
        
    return False


n, r, c = map(int, input().split())

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

x, y = r-1, c-1

result = [arr[x][y]]

while True:
    # move 함수 호출 통해 global var로 설정한 x, y 갱신
    move_ = move()
    
    # 더 이상 이동할 곳이 없다.
    if not move_:
        break
    
    result.append(arr[x][y])

for r in result:
    print(r, end=' ')
