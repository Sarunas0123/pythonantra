def fun_1():
    a = [ 1, 2 ,3 ,3, 6, 7, 8, 8, 7]
    b = []
    for i in a:
        if i not in b:
            b.append(i)
    return print(b)

fun_1()

def fun_2():
    a = [1, 2, 3, 4, 5, 5, 5, 2, 3, 4]
    number = set()

    for x in a:
        number.add(x)
    return print(number)
fun_2()