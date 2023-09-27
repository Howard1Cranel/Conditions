a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))

if a == b or a == c or b == c:
    print("Ошибка")
else:
    if (a < b and b < c) or (c < b and b < a):
        print(f"Число {b} стоит между числами {a} и {c}")
    elif (b < a and a < c) or (c < a and a < b):
        print(f"Число {a} стоит между числами {b} и {c}")
    elif (a < c and c < b) or (b < c and c < a):
        print(f"Число {c} стоит между числами {a} и {b}")
