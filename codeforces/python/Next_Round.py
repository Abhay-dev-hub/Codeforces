x,y = map(int,input().split())
z = list(map(int,input().split()))
count = 0
for i in z:
    if z[y - 1] <= i and i > 0:
        count += 1
print(count)
        





    

