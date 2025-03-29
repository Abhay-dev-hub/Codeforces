t = int(input())
num = list(map(int,input().split()))
add = 0
for i in range(0,t):
    add += num[i]
print((max(num)*t)-add)
