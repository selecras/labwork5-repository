from random import randint
from time import sleep


def y_n(text: str) -> bool:
    ans = input(text).lower()
    while ans not in ("y", "n"):
        print("Некорректный ввод")
        ans = input(text).lower()
    if ans == "y":
        return True
    return False


num = randint(1000, 9999)
print('Игра "Быки и коровы" (отечественный wordle)')
sleep(1)
print("Компьютер загадал четырёхзначное число")
sleep(1)
print("Ваша задача -- угадать его")
sleep(1)
print(
    "При каждой попытке, компьютер сообщает вам количество:\n1) Быков (цифра есть и она на своем месте)\n2) Коров (цифра есть, но не на своем месте)"
)
print()
sleep(1)

atts = []
print(num)
previous = []

while True:
    cows = 0
    bulls = 0
    used_j = []
    used_i = []
    try:
        guess = int(input("Введите число: "))
        if not (1000 <= guess <= 9999):
            raise ValueError
    except ValueError:
        print("Некорректный ввод")
        continue
    atts.append(guess)

    if guess == num:
        previous.append((guess, atts.copy()))
        print(
            f"Поздравляю! Вы угадали число {num}.\nКоличество попыток: {len(atts)}.\n"
        )
        sleep(1)
        check_prevs = y_n("Посмотреть предыдущие игры? (y/n): ")
        if check_prevs:
            for i, prev in enumerate(previous, 1):
                print(
                    f"{i}) Загаданное число: {prev[0]}\nКоличество попыток: {len(prev[1])}"
                )
                for j, att in enumerate(prev[1], 1):
                    print(f"Попытка {j}) {att}")
                print()

        ans = y_n("Сыграть еще раз? (y/n): ")
        if ans:
            num = randint(1000, 9999)
            print(num)
            atts = []
            print("Тогда играем еще раз.")
        else:
            break

    else:
        for i, digit in enumerate(str(num)):
            for j, r_digit in enumerate(str(guess)):
                if j not in used_j and i not in used_i:
                    if digit == r_digit and i == j:
                        bulls += 1
                        used_j.append(j)
                        used_i.append(i)
                    elif digit == r_digit:
                        cows += 1
                        used_j.append(j)
                        used_i.append(i)
        print(f"Коровы: {cows}\nБыки: {bulls}\n")
# fds