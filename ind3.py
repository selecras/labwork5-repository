from random import randint


def bubble_sort(lst: list) -> list:
    n = len(lst)
    for i in range(n - 1):
        flag = False
        for j in range(n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                flag = True
        if not flag:
            break
    return lst

if __name__ == "__main__":
    print("""Пузырьковая сортировка
    Режимы работы:
    1. Ввести массив вручную
    2. Случайный массив из N элементов
    """)
    ans = input("Ваш выбор: ")

    while ans not in ("1", "2"):
        print("Некорректный ввод")
        ans = input("Ваш выбор: ")

    if ans == "1":
        while True:
            try:
                lst = list(map(float, input("Введите числа через пробел: ").split()))
                break
            except ValueError:
                print("Некорректный ввод")
    elif ans == "2":
        while True:
            try:
                n = int(input("Введите количество элементов: "))
                if not (1 <= n <= 1000):
                    raise ValueError

                a = int(input("Введите нижнюю границу: "))
                b = int(input("Введите верхнюю границу: "))
                if a >= b:
                    raise ValueError

                break
            except ValueError:
                print("Некорректный ввод")
        lst = [randint(a, b) for _ in range(n)]

    sorted_list = bubble_sort(lst)

    print("Отсортированный массив: ", end="")
    print(*sorted_list, sep=", ")
