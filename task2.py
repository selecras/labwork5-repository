n = int(input("Введите N: "))

sum_numbers = 0
product = 1
sum_squares = 0

for i in range(1, n + 1):
    sum_numbers += i
    product *= i
    sum_squares += i**2

print(f"""Сумма: {sum_numbers}
Произведение (N!): {product}
Сумма квадратов: {sum_squares}""")
