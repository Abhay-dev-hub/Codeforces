t = int(input())
game_results = input()

count_Anton = 0
count_Danik = 0

for result in game_results:
    if result == 'A':
        count_Anton += 1
    elif result == 'D':
        count_Danik += 1

if count_Anton > count_Danik:
    print("Anton")
elif count_Danik > count_Anton:
    print("Danik")
else:
    print("Friendship")
