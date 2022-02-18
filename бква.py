word = input()
letter = int(input())
if letter < 0 or letter > len(word):
    print("ERROR")

else:
    print(word[letter-1])
