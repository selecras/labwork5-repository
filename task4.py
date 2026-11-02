n = int(input("Введите число: "))
original = n
factors = []

divisor = 2
while divisor * divisor <= n:
    while n % divisor == 0:
        factors.append(divisor)
        n //= divisor
    divisor += 1

if n > 1:
    factors.append(n)

print(f"{original} = {' * '.join(map(str, factors))}")
