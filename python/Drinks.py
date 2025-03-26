drinks = int(input())
vol = list(map(int,input().split()))
sum = 0
for i in range(0,len(vol)):
    sum += vol[i]
print(sum/drinks)
