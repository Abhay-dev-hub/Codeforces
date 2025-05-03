t = int(input())
for _ in range(0,t):
    jar = int(input())
    i = 0
    while True:
        q = ((i+i)*3//4)//3
        if q == jar:
            break;
        i += 1
    print(i)