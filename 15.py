def stringify():
    sen = input("Write a sentence!\n")
    split = sen.split()
    rev = split[::-1]
    join = " ".join(rev)
    return print(join)

stringify()