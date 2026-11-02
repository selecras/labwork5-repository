from math import sin, pi

print(f"{'x':>8} {'sin(x)':>10}")
print("-" * 20)

for i in range(11):
    x = i * pi / 10
    y = sin(x)
    print(f"{x:8.4f} {y:10.4f}")
