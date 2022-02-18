number = int (input(": "))
count = 0
flag = False
sum_ = 1
while sum_ < number:
    if flag == True:
        sum_ = sum_ * 2
        flag = False
    else:
        sum_ += 1
        flag = True
    count += 1
print (count)
