pos_i = 0
pos_j = 0
# arr = list(map(int,input().split()))
for i in range(0,5):
    arr = list(map(int,input().split()))

    for j in range(0,5):
        if arr[j] == 1:
            pos_j = j
            pos_i = i
print(abs(pos_j - 2)+abs(pos_i - 2))
