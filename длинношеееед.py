str = input().lower()
sub = 'д'
count = 0

for i in range(len(str)):
    if str.count(str[i]) > count:
        count = str.count(str[i])
print(count)
