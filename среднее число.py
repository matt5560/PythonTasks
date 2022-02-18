count = 0
sum1 = 0
while True:
    num1 = int(input("введите числo:"))
    count += 1
    sum1 += num1
    if num1 < -300:
        break
    
print(sum1 / count)




