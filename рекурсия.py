def reverse():
    numbers = int(input())
    if numbers != 0:
        reverse()
        print(numbers)

reverse()
