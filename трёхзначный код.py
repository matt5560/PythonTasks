code_ = int (input ("введите трёхзначный код: "))
code1_ = code_ // 100
code2_ = code_ // 10 % 10
code3_ = code_ % 10

if code1_ == code2_ and code1_ == code3_ :
    print ("в числе все цифры одинаковые")

elif code1_ == code2_ or code2_ == code3_ or code1_ == code3_ :
    print ("в числе две одинаковые цифры")

else:
    print ("OK")







