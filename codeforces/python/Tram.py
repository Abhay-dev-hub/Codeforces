t = int(input())
count = []
p = 0
for i in range(0,t):
    x,y = map(int,input().split())
    if i == 0:
        capacity = y
        count.append(capacity)
        continue  
    capacity += y 
    capacity-= x
    
    count.append(capacity)
print(max(count))
    
