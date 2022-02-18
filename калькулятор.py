num1_ = float (input ("введите число "))

num2_ = float (input ("введите число "))

sign_ = input ("введите знак ")

if sign_ == ("+"):
    print (num1_ + num2_)
elif sign_ == ("-"):
    print (num1_ - num2_)
elif sign_ == ("*"):
    print (num1_ * num2_)
elif num2_ == 0 and sign_ == ("/"):
    print ("888888")
elif sign_ == ("/"):
    print (num1_ / num2_)

else:
    print ("888888")
