order = input()

# 동 남 서 북
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

x, y = 0, 0

# 리스트는 0부터 시작된다는 것 기억
dir_num = 3
for i in order:
    if i == 'L':
        dir_num = (dir_num - 1 + 4) % 4
    
    elif i == 'R':
        dir_num = (dir_num + 1) % 4

    else:
        x += dx[dir_num]
        y += dy[dir_num]

print(x, y)
