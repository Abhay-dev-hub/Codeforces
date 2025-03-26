#time exceeded 1000ms
#dont know how to optimize this shi


t = int(input())
for _ in range(0,t):
    a , b = map(int,input().split())
    if a % b == 0:
        print(0)
    else:
        print(b - a % b)
