n = int(input("Введите число: "))
original = n

count = 0
total = 0
product = 1
reversed_num = 0

while n > 0:
    digit = n % 10
    count += 1
    total += digit
    product *= digit
    reversed_num = reversed_num * 10 + digit
    n //= 10

print(f"""Количество цифр: {count}
Сумма цифр: {total}
Произведение цифр: {product}
Перевёрнутое число: {reversed_num}""")
