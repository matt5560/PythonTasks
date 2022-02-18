num = 0
num1 = 0
range_ = int(input("введите кол. чисел:"))
for i in range(1, range_+1):
    num1 = int(input())
    
    if i % 2 != 0:
        num += num1
    else:
        num -= num1
        
    
print(num)
