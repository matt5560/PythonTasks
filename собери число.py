num=int(input())
num1=num//100
num2=num//10%10
num3=num%10

num12 = num1 + num2
num23 = num2 + num3

if num12 > num23:
    print (num12,num23)
else:
    print (num23,num12)

