import math

a = float(input("Введите значение переменной a:"))
b = float(input("Введите значение переменной b:"))
c = float(input("Введите значение переменной c:"))

d = b*b - 4 * a * c
if d >= 0:
    d = math.sqrt(d)
    if d > 0:
        print("x1 =", (-b + d)/(2 * a))
        print("x2 =", (-b - d)/(2 * a))
    elif d == 0:
        print("x = ", -b/(2*a))
else:
    print("корней нет")
