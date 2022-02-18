number_ = int (input ("введите трёхзначное число: "))
number1_ = number_ // 100
number2_ = number_ // 10 % 10
number3_ = number_ % 10

if number1_ == number2_ or number1_ == number3_ or number2_ == number3_:
    print ("жаль, вы ввели обычное число")

elif number1_ < number2_:
    if number2_ < number3_:
        highest_num = number3_
    else:
        highest_num = number2_


if number1_ < number3_:
    highest_num = number3_
elif number1_ > number3_:
    highest_num = number1_




elif number1_ > number2_:
    if number2_ > number3_:
        lowest_num = number3_
    else:
        lowest_num = number2_

if number1_ > number3_:
    lowest_num = number3_
elif number1_ < number3_:
    lowest_num = number1_

        

elif number1_ > number2_:
    if number2_ < number3_:
        mid_num = number2_
    else:
        mid_num = number3_


if number1_ < number3_:
    mid_num = number1_
elif number1_ > number3_:
    mid_num_ = number3_




elif lowest_num / 2 + highest_num / 2 == mid_num:
    print ("это число красивое")
else:
    print ("жаль, вы ввели обычное число")







