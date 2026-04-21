t = int(input())

for _ in range(0,t):
    len = int(input())
    arr = list(map(int,input().split()))
    rep = 0
    maxi = 0
    for i in arr:
        if i == 0:
            rep += 1
            maxi = max(maxi,rep)
        if i == 1:
            rep = 0
        
    print(maxi)