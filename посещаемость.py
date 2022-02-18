
date = 1


days = int(input("days : "))

print("day: ", date)
date += 1
students = int(input("number of students: "))
set_name=[set(input() for i in range(students)) for j in range(days)]
res = set_name[0]
for i in range (set_name):
    print(res.intersection(i))
     
