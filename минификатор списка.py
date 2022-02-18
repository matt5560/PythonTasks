shoppinglist = int(input())
list_names = []
list_count = []
for i in range(shoppinglist):
    list_names.append(input())
    list_count.append(int(input()))
for j in range(len(list_count)):
    print(list_count[len(list_count)-1-j], list_names[len(list_names) - 1 - i])

