s = int(input())
count = 0
brat_1 = [int(input()) for i in range(s)]
brat_2 = brat_1[:]
train_num = int(input())
for i in range(train_num):
    brat_num = int(input())
    skill_ = int(input())
    trenirovki_ = int(input())

    if brat_num == 1:
        brat_1[skill_] += trenirovki_
    elif brat_num == 2:
        brat_2[skill_] += trenirovki_
print(*brat_1)
print(*brat_2)
for i,j in zip(brat_1, brat_2):
    if i == j:
        count += 1
print(count)