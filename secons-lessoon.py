# ------------1--------------
# name = int(input("What is your name?"))
# age = input("what is your age?")
# how_much = input("enter a number, how many time u want to repeat a messege")
# year_when_100 = 2021 - age + 100
# print("you will be 100 in" + str(year_when_100))
# -------------------2-------------
#
# number = int(input("enter a number"))
#
# if number % 2 == 0:
#     print("number is even")
# else:
#     print("number is odd")
#------------2.2---------
# number1 = int(input("input the first number: "))
# number2 = int(input("input the first number: "))
#
# if number1 % number2 == 0:
#     print("number is even")
# else:
#     print("number is odd")
#--------3-----------
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = []
# counter = 0
# eina = 0
# for item in a:
#     if item < 5:
#         b.append(item)
# print(b)
#-------------4---------
number = int(input("input a number"))
x = range(1, number + 1)
new_array = []
for item in x:
    if number % item == 0:
        new_array.append(item)
print(new_array)
