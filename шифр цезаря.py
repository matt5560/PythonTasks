number = int(input())
sentence = input()
alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЭЮЯ"
result = ""
shiftedAlphabet = alphabet[number:]+alphabet[0:number]

for i in range(len(sentence)):
    char = sentence[i]
    letter = alphabet.find(char.upper())
    if letter == -1:
        result += char
    elif char.islower():
        result += shiftedAlphabet[letter].lower()
    else:
        result += shiftedAlphabet[letter]


print(result)
