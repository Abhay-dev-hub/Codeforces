t = int(input())
word = str(input())
boo = True
for i in range(0,t-1):
    if t <= 1:
        boo = False
        break 

    elif word[i] == word[i+1]:
        boo = False
    

if boo == False:
    print("NO")
else:
    print("YES")
