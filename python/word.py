x = input()
low = 0
up = 0
for i in x:
    if i == i.lower():
        low += 1
    else:
        up += 1

if low >= up:
    print(x.lower())
else:
    print(x.upper())


