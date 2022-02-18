sign = input()
input_text = input()
list_text = input_text.split(" ")

for i in range(len(list_text)):
    if list_text[i].find(sign) != -1 or list_text[i].find(sign.upper()) != -1:
        print(list_text[i])