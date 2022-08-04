N = int(input())

arr = [
    list(map(int, input().split()))
    for _ in range(N)
]

def coin_count(row_s, row_e, col_s, col_e):
    coin = 0
    # 3X3을 탐색할 수 있도록 수정
    for row in range(row_s, row_e+1):
        for col in range(col_s, col_e+1):
            coin += arr[row][col]
    
    return coin

coin = 0

# 예시 문제와 달리 해당 문제는 3X3이므로 고려 필요
# 함수를 변경하여 해결
for i in range(N-2):
    for j in range(N-2):
        coin_num = coin_count(i, i+2, j, j+2)

        coin = max(coin, coin_num)

print(coin)
