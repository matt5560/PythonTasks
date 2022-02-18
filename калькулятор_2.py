


def sum_(a,b):
    return a + b

def min_ (a,b):
    return a - b

def mul_ (a,b):
    return a * b

def div_ (a,b):
    if b == 0:
        print("Error")
    else:
        return a / b
def mod_ (a,b):
    if b == 0:
        print("Error")
    else:
        return a % b

while True:   

    num1 = int (input ("введите число "))

    num2 = int (input ("введите число "))

    sign_ = input ("введите знак ")

    if sign_ == "+":
        sum_(num1,num2)
        print(sum_ (num1,num2))

    elif sign_ == "-":
        min_(num1,num2)
        print(min_ (num1,num2))

    elif sign_ == "*":
        mul_(num1,num2)
        print(mul_ (num1,num2))

    elif sign_ == "/":
        div_(num1,num2)
        print(div_ (num1,num2))

    elif sign_ == "%":
        mod_(num1,num2)
        print(mod_ (num1,num2))

    elif sign_ == "!":
        break
