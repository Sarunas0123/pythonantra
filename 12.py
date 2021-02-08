import random

def list_fun():
    d = []
    c = random.randint(1, 15)
    a = random.sample(range(100), c)
    print(a)
    lenght = len(a)
    d.append(a[0])
    d.append(a[lenght - 1])
    return print(d)

list_fun()