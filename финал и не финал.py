n = int(input())
list_team = []
for i in range(n):
    name = input()
    points = int(input())
    list_team.append((name, points))
len_list_team = len(list_team)
for i in range(len_list_team - 1):
    for g in range(len_list_team - i - 1):
        if list_team[g][1] > list_team[g + 1][1]:
            list_team[g], list_team[g + 1] = list_team[g + 1], list_team[g]
final_team = list_team[(len_list_team // 2):]
lost_team = list_team[:(len_list_team // 2)]
len_final_team = len(final_team)
for i in range(len_final_team - 1):
    for g in range(len_final_team - i - 1):
        if final_team[g] > final_team[g + 1]:
            final_team[g], final_team[g + 1] = final_team[g + 1], final_team[g]
len_lost_team = len(lost_team)
for i in range(len_lost_team - 1):
    for g in range(len_lost_team - i - 1):
        if lost_team[g] > lost_team[g + 1]:
            lost_team[g], lost_team[g + 1] = lost_team[g + 1], lost_team[g]

print(final_team)
print(lost_team)

for u in final_team:
    print(u[0])
for y in lost_team:
    print(y[0])