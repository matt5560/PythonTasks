list1_= []

for u in range (int(input())):
    list1_.append (int(input()))
for i in range (0, len(list1_)-1):
    if list1_[i] > 0 and list1_[i+1] > 0:
        print(list1_[i],list1_[i+1])
        break
    elif list1_[i] < 0 and list1_[i+1] < 0:
        print(list1_[i],list1_[i+1])
        break
    
