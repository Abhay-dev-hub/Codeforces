t = int(input())

for _ in range(0,t):
    count = 0
    string = str(input())
    if string[0] != 'a':
        count += 1
    if string[1] != 'b':
        count += 1
    if string[2] != 'c':
        count += 1
    if count < 3:
        print("YES")
    else:
        print("NO")
