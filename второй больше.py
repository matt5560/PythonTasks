num = []
num2 = []
flag = True
count = 0
currentNum = -1
while  currentNum != 0:
    currentNum = int(input())
    count += 1
    num.append (currentNum)
for i in range (len(num)-1):
    for j in range (len(num)-i-1):
        if num[j] > num[j+1]:
            num[j],num[j+1] = num[j+1], num[j]
print(num[j-2])
                
    
