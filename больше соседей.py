n = int(input())
count = 0
list1_ = []
for b in range(n):
    list1_.append (int(input()))
    
for i in range(1, len(list1_)-1):
    if list1_[i] > list1_[i+1] and list1_[i] > list1_[i-1]:
        count += 1
print(count)

