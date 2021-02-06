inp = input("Give a random word!\n")
rev = inp[::-1]

if inp.lower() == rev.lower():
    print(inp, " is a palindrome!")
else:
    print(inp, " is not a palindrome!")