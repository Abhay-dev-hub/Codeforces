guest = list(input())
host = list(input())
pile = list(input())

x = sorted(guest+host)
pile = sorted(pile)

if pile == x:
    print("YES")
else:
    print("NO")
