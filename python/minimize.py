t = int(input())
for i in range(0,t):
    a,b = map(int,input().split())
    if a == b:
        print(0)
    else:
        c = b - a
        print((c-a)+(b-c))
