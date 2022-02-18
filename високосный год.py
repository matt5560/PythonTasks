year_ = int (input ("введите год: "))
if year_%4 == 0 and year_%4 != 100 or year_%400 == 0:
    print ("високосный")
else:
    print ("не високосный")
