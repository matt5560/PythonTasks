def power(a,n):
    count = 1
    for i in range (n):
        count = count * a
    if n > 0:
        return count
    else:
        return 1/count



a = int(input("a_ "))
n = int(input("n_ "))


power(a,n)
print(power(a,n))


