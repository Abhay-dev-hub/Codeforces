t = int(input())
for q in range(0,t):
    x = int(input())
    if x <= 1399:
        print("Division 4")
    elif 1400 <= x <= 1599:
        print("Division 3")
    elif 1600 <= x <= 1899:
        print("Division 2")
    else:
        print("Division 1")
