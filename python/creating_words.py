t = int(input())
for _ in range(0,t):
    x,y = map(str,input().split())
    xi = y[0] + x[1:]
    yi = x[0] + y[1:] 
    print(xi,yi)
    
