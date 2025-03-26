t = int(input())
for _ in range(0,t):
    y = int(input())
    num = list(map(int,input().split()))
    for i in range(0,y-1):
        if num[i] != num[i+1]:
            print(i)
            break;
