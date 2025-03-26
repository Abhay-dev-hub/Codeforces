t = int(input())
for _ in range(0,t):
    l,r,d,u = map(int,input().split())
    if l == r == d == u:
        print("YES")
    else:
        print("NO")
