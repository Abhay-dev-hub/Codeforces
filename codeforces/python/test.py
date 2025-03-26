t = int(input())
for p in range(0,t):
    x = int(input())
    cycles = x // 15
    rem = x % 15
    count = cycles * 3  
    
    for i in range(x - rem, x + 1):
        if i % 3 == i % 5:
            count += 1

    print(count)



