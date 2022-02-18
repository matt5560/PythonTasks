dishes_num = int(input())
set_dishes_1 = set()
set_dishes_2 = set()

for i in range(dishes_num):
    dishes = input()
    set_dishes_1.add(dishes)
days = int(input())

for j in range(days):
    daily_dishes_num = int(input())
    for k in range(daily_dishes_num):
        daily_dishes = input()
        set_dishes_2.add(daily_dishes)

print(set_dishes_1 - set_dishes_2)


