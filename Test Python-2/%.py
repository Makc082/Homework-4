# a - позитивні, b - негативні, z - нуль, p - парні, n - не парні.

import random

num = [random.randint(-100, 100) for i in range(100)]

print(num)

a = 0
b = 0
z = 0
p = 0
n = 0

for x in num:
    if x > 0:
        a += 1
    elif x < 0:
        b += 1
    else:
        z += 1

    if x % 2 == 0:
        p += 1
    else:
        n += 1

print(f"Позитивні числа: {a}%")
print(f"Негативні числа: {b}%")
print(f"Нуль: {z}%")
print(f"Парні числа: {p}%")
print(f"Не парні числа: {n}%")