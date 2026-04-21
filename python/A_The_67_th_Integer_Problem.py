t = int(input())

for _ in range(0,t):
    car = 0
    num = int(input())
    if num > 0:
      car = num+1
    print(min(car,67))