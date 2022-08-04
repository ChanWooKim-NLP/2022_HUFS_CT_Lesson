n, t = map(int, input().split())

arr = []

# 입력된 리스트들을 1차원으로 펼침
for _ in range(3):
    arr.extend(list(map(int, input().split())))

# 마지막 수 저장, 뒤에서부터 당겨서 회전
def rotate():
    temp = arr[-1]

    for i in range(len(arr)-1, 0, -1):
        arr[i] = arr[i-1]
    
    arr[0] = temp

for _ in range(t):
    rotate()

# 삼각형이므로 줄바꿈 기준은 전체 1차원 리스트 길이에서 3을 나눈 몫
split = len(arr) // 3
arr_1 = arr[:split]
arr_2 = arr[split: split*2]
arr_3 = arr[split*2:]

for i in arr_1:
    print(i, end=' ')
print()

for i in arr_2:
    print(i, end=' ')
print()

for i in arr_3:
    print(i, end=' ')
