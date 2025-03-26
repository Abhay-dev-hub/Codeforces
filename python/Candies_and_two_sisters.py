t = int(input())
for q in range(0,t):
    x = int(input())
    if x == 1 or x == 2:
        print(0)
    elif x % 2 == 0:
        print(int((x / 2) - 1))
    else:
        print(int((x/2) - 0.5))
