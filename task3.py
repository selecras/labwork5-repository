n = int(input("Введите N: "))

a, b = 0, 1
print(f"Первые {n} чисел Фибоначчи:")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

print()
