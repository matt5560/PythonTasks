string = input()
count = 1
for i in range(len(string)-1):
    if string[i] == string[i+1]:
        count += 1
    else:
        exist = string[i]
        print(count, " ", string[i])
        count = 1
print(count, " ", string[i])
