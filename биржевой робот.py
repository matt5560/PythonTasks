a = []
start = 1
while start != 0:
    start = (int(input()))
    a.append (start)
for i in range (len(a)-1):
    if a[i+1] > a[i]:
        buy = a[i+1]
        break
for y in range (len(a)-1):
    if a[y+1] < a[y]:
        sell = a[y+1]
        break
print("покупка",buy)
print("продажа",sell)
print("общий доход",sell - buy)
        
        
    







