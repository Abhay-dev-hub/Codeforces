t = int(input())
for q in range(0,t):
    x = int(input())
    if x % 3 != 0 or str(x[-1]) != 3:
        print(x)
