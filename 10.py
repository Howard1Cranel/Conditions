import math
a = float(input("Введите коэффициент a: "))
b = float(input("Введите коэффициент b: "))
c = float(input("Введите коэффициент c: "))

discriminant = b**2 - 4*a*c

if discriminant > 0:
    x1 = (-b + math.sqrt(discriminant)) / (2 * a)
    x2 = (-b - math.sqrt(discriminant)) / (2 * a)
    if x1 == x2:
        print(f"Корни уравнения: {x1}, {x2}. Корни совпадают")
    print("Корни уравнения:", x1, x2)
elif discriminant == 0:
    x = -b / (2 * a)
    print("Уравнение имеет один корень:", x)
else:
    print("Уравнение не имеет корней")