cost, money, bananas = map(int, input().split())

total_cost = cost * (bananas * (bananas + 1) // 2)

needed = max(0, total_cost - money)

print(needed)


