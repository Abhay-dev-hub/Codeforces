t = int(input())

for _ in range(0,t):
    length = int(input())
    name = input()

    if sorted(name) == sorted("Timur"):
        print("YES")
    else:
        print("NO")