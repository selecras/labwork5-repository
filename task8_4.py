def prime_nums(n):
    ignore = []
    result = []
    for i in range(2, n + 1):
        if i in ignore:
            continue
        for j in range(i, n + 1):
            if j % i == 0:
                ignore.append(j)
        result.append(i)
    return result


MAX = 10**6
while True:
    try:
        n = int(input("Введите число N: "))
        if not (2 <= n <= MAX):
            raise ValueError
        break
    except ValueError:
        print("Некорректный ввод")

res = prime_nums(n)
print(f"Список простых чисел до {n} включительно:", end=" ")
print(*res, sep=", ", end=".")
