def block_del(arr, s, e):
    del_arr = []

    arr[s-1:e] = [0] * (e -s-1)
    end_array = len(arr)

    for i in range(end_array):
        if arr[i] != 0:
            del_arr.append(arr[i])
    
    return del_arr

n = int(input())

block_num = [
    int(input())
    for _ in range(n)
    ]

for _ in range(2):
    s, e = map(int, input().split())
    block_num = block_del(block_num, s, e)

print(len(block_num))
for b in block_num:
    print(b)
