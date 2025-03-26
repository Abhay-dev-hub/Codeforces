t,height = map(int,input().split())
num = list(map(int,input().split()))
count = 0
for digit in num:
    if digit > height:
        count += 2
    else:
        count += 1
print(count)

