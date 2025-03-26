t = int(input())
num = input()
num = num.replace(" ","")        
one = 0
zero = 0
for i in num:
    if i == '1':        
        one += 1
    else:
        zero += 1
    
if one != 0:
    print("HARD")
else:
    print("EASY")
