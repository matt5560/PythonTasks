word = input()
favnum = int(input())
letter = input()
if len(letter) > len(word) or len(letter) > 1:
    print("ошибка")
elif word[favnum-1] == letter:
    print("да")
else:
    print("нет")
