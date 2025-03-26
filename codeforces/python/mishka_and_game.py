t = int(input())
mishka = 0
chris = 0
for _ in range(0,t):
    x,y = map(int,input().split())
    if x > y:
        mishka += 1
    elif y > x:
        chris += 1

if mishka > chris:
    print("Mishka")
elif chris > mishka:
    print("Chris")
else:
    print("Friendship is magic!^^")
