d = int (input ("введите число: "))
m = int (input ("введите месяц: "))
year = int (input ("введите год: "))
c = year // 100
y = year % 100

print (d+((13*m-1)//5)+y+((y//4)+(c//4)-2*c+777)%7)

