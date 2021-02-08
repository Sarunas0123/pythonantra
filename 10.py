import random
c = random.randint(1, 10)
d = random.randint(1, 10)
a = random.sample(range(100), c)
b = random.sample(range(100), d)
c = []

c = [x for x in a if x in b]
print(a)
print(b)
print(c)