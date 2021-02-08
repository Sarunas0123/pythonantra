def int_odd():
    number = int(input("input a number:\n"))
    if number % 2 == 0:
        return print("nuber ", number, " is not a prime")
    else:
        return print("nuber ", number, " is a prime")

int_odd()