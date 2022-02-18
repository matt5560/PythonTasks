line_count = int(input())
moda = []
mediana = []
all = []

for i in range(line_count):
    s = list(map(int, input().split()))
    s.sort()
    middle = float(len(s)) / 2
    middle___ = s[int(middle - .5)]
    mx = 0
    nxx = 0
    for j in s:
        if s.count(j)>mx:
            mx = s.count(j)
            nxx = j
    mediana.append(middle___)
    moda.append(nxx)
    for i in s:
        all.append(i)
all.sort()
print(*mediana)
print(*moda)
mediana.sort()
moda.sort()
middle_med = float(len(mediana)) / 2
med___ = mediana[int(middle_med - .5)]

middle_mod = float(len(moda)) / 2
mod___ = moda[int(middle_mod - .5)]

middle_all = float(len(all)) / 2
all___ = all[int(middle_all - .5)]

print(med___)
print(mod___)
print(all___)