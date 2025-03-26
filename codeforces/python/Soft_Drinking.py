n,k,l,c,d,p,nl,np = map(int,input().split())
drinks = k * l
toasts = drinks // nl
lime = c * d 
salt = p // np

print(min(toasts,lime,salt)//n)
