col = int(input("число строк"))

for i in range(col):
    word = input()
    if word.find("кот") != -1 or word.find("КОТ") != -1:
        print("МЯУ")
    else:
        print("НЕТ")

    
