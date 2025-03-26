t = int(input())

for i in range(0,t):
    a,b,c = map(int,input().split())
    if a + b == c or a + c == b or c + b == a:
        print("YES")

    else:
        print("NO")
