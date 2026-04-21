t = int(input())

for i in range(0,t):
    string = str(input())
    count = 0
    for i,chr in enumerate("codeforces"):
        if string[i] != chr:
            count += 1
    print(count)

