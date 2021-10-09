import numpy as np

print("Попробуйте угадать число")
n = np.random.randint(1, int(input("Введите кол-во чисел: "))+1)
k = int(input("Введите кол-во попыток: "))

print("Поехали!")
c = k
for i in range(1, k+1):
    x = int(input())
    if x == n:
        print("Вы угадали!")
        break
    elif x < n:
        print("Загаданное число больше")
        c -= 1
        print("У вас осталось", c, "попыток")
    elif x > n:
        print("Загаданное число меньше")
        c -= 1
        print("У вас осталось", c, "попыток")
if c == 0:
    print("Вы проиграли, я загадал", n)
