n = int(input("Введите число: "))
revs = 0

temp = n
while temp > 0:
    digit = temp % 10
    revs = revs * 10 + digit
    temp //= 10

if n == revs:
    print(f"{n} -- палиндром")
else:
    print(f"{n} -- не палиндром")
