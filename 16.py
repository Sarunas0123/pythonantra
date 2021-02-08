import random
import string

def strong_password(length):
    password_cha = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(password_cha) for i in range(length))
    return print("Your strong password is: ", password)

def weak_password(length):
    letters = string.ascii_letters
    result_str = ''.join(random.choice(letters) for i in range(length))
    return print("Your weak password is: ", result_str)

print("Welcome to random password generator!\n")

while True:
    state = input("Which would you prefer? strong or weak password?\n")
    stat = state.lower()
    length = input("How long you want your password to be?\n")

    if stat == "weak" and length.isnumeric():
        weak_password(int(length))
    elif stat == "strong" and length.isnumeric():
        strong_password(int(length))
    else:
        print("Wrong input!")

    b = input("Do you want another password? y/n\n")
    if b.lower() == "y":
        continue
    else:
        break