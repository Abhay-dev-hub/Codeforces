t = int(input())
count = 0
for q in range(0,t):
    x = str(input())
    if x == "X++" or x == "++X":
        count += 1
    if x == "--X" or x == "X--":
        count -= 1
print(count)
