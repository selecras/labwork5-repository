n = 5

print("Прямоугольник:")
for _ in range(n):
    print("*" * n)

print("\nТреугольник:")
for i in range(1, n + 1):
    print("*" * i)

print("\nЁлочка")
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))

print("\nРомб")
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))
