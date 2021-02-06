import random

a = random.randint(1, 9)
inp = input("Guess the number form 1 to 9\n")
counter = 0

while True:
    counter =+ 1
    if inp not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        print("Wrong input!\n")
    elif str(a) == inp:
        print("You guessed the number!\n")
        print("It took you ", counter, " times")
        break
    elif str(a) > inp:
        print("you guessed too low!\n")
    elif str(a) < inp:
        print("you guessed too high!\n")

    b = input("Do you want to continue guessing? y/n\n")
    if b.lower() == "y":
        inp = input("Guess the number form 1 to 9\n")
        continue
    else:
        break