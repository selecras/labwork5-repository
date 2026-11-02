from decimal import Decimal


def factorial(num: int) -> int:
    res = 1
    for i in range(1, num + 1):
        res *= i
    return res


def get_e(accuracy: int) -> Decimal:
    e = 1
    for i in range(1, accuracy + 1):
        e += Decimal(1) / Decimal(factorial(i))
    return e


print("Вычисление числа Эйлера")

while True:
    try:
        acc = int(input("Задайте точность вычисления: "))
        if not (0 <= acc <= 10**6):
            raise ValueError
        break
    except ValueError:
        print("Некорректный ввод")

e = get_e(acc)
print(f"Вычисленное число e = {e}")
