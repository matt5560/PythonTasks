workers = int(input("введите кол. человек: "))
set_names_1 = set()
set_names_2 = set()

for i in range(workers):
    names = input()
    if names in set_names_1:
        set_names_2.add(names)
    else:
        set_names_1.add(names)
        
result = set_names_1 - set_names_2

print(workers - len(result))



