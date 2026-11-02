from random import uniform

MAX = 10_000_000

while True:
    try:
        n = int(input("Введите количество точек (влияет на точность): "))
        if not (1 <= n <= MAX):
            raise ValueError
        break
    except ValueError:
        print(f"Некорректный ввод (1 <= n <= {MAX})")

k = 0

for _ in range(n):
    x, y = uniform(-1, 1), uniform(-1, 1)
    if x * x + y * y <= 1:
        k += 1

pi = 4 * k / n
print(f"Приближенное значение π = {pi} (при n = {n})")
