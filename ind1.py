from random import randint
from time import sleep
from collections import Counter

def y_n(text: str) -> bool:
    while True:
        ans = input(text).lower()
        if ans in ("y", "n"):
            return ans
        print("Некорректный ввод")


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
previous = []

while True:
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
            atts = []
            print("Тогда играем еще раз.")
        else:
            break

    else:
        num_s = str(num)
        guess_s = str(guess)
        c_num = Counter(num_s)
        c_guess = Counter(guess_s)
        total = sum([min(c_num[d], c_guess[d]) for d in c_num])

        bulls = sum([a == b for a, b in zip(str(guess_s), str(num_s))])
        cows = total - bulls
        print(f"Коровы: {cows}\nБыки: {bulls}\n")