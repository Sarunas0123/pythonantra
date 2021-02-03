a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6 , 7, 8, 9, 10, 11, 12, 13]

lenght = min(len(a), len(b))
c = []
i=0
while i<lenght:
    if a[i] in b:
        if a[i] not in c:
            c.append(a[i])
    i += 1

print(c)