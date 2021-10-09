a = int(input("Введите число:"))
if a % 5 == 0 and a % 7 == 0:
    print("11")
else:
    if a % 5 == 0:
        print("01")
    elif a % 7 == 0:
        print("10")
    else:
        print("00")
