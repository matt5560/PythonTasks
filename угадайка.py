flag_ = False
min_ = 1
max_ = 1000

while not flag_:
    mid_ = (max_ + min_) // 2
    print("ваше число: ", mid_, "?")
    inpt = input(": ")
    if inpt == ">":
        min_ = mid_
    elif inpt == "<":
        max_ = mid_
    else:
        flag_ = True
        print("ура я нашёл его!")
        

