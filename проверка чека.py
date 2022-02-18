n = input()
number, default_summ = int(n[:4]), int(n[4:])
allprice = []
itog = 0
summ1 = 0
s_kaknibut = []
for i in range(number):
    p = input()
    price, count, summ = int(p[:7]), int(p[8:12]), int(p[13:])
    if price * count != summ:
        s_kaknibut.append(i+1)
    summ1 = price * count
    allprice.append(summ1)

for j in allprice:
    itog += j
print(default_summ - itog)

for u in s_kaknibut:
    print(u)