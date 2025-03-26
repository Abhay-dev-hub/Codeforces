x = int(input()) 
steps = (x // 5) + (1 if x % 5 != 0 else 0)
print(steps)
