line_num = int(input())
final_list = []

for i in range(line_num):
    ingredients = input()
    if ingredients.find("лук") == -1:
        final_list.append(ingredients)
print(",".join(final_list))
