t = int(input())

for _ in range(0,t):
    num = list(map(int,input().split()))
    num.sort()
    print(num[1])