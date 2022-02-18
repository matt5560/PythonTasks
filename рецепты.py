ingredients = int(input())
set_ingredients = set()


for i in range(ingredients):
    ingredients_names = input()
    set_ingredients.add(ingredients_names)
    
recept = int(input())

for j in range(recept):
    recept_name = input()
    recept_ing_number = int(input())
    set_recept_ing = set()
    
    for k in range(recept_ing_number):
        recept_ing = input()
        set_recept_ing.add(recept_ing)
    if len(set_recept_ing & set_ingredients) == len(set_recept_ing):
        print(recept_name)
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
