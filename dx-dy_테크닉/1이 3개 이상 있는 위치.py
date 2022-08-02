def in_range(x, y, n):
    return 0 <= x and x < n and 0 <= y and y < n

n = int(input())

'''
# 2차원 입력에 대한 리스트 컴프리헨션
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]
'''

arr = []
for _ in range(n):
    arr_list = list(map(int, input().split()))
    arr.append(arr_list)

ans = 0
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0] 
for x in range(n):
    for y in range(n):
        cnt_xy = 0
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            if in_range(nx, ny, n) and arr[nx][ny] == 1:
                cnt_xy += 1

        if cnt_xy >= 3:
            ans += 1

print(ans)
