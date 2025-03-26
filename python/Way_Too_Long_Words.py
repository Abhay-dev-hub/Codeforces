t = int(input())
for i in range(0,t):
    x = input()
    if len(x) <= 10:
        print(x)
        i += 1

    else:
        p = len(x) - 2
        u = x[0] 
        r = x[len(x)-1]
        print(f"{u}{p}{r}")
        i += 1
