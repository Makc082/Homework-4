#n - кілкість ярусів, x - висота стовбура, y - ширина стовбура.
import os
os.system("cls")

n = 5
x = 5
y = 3 

for i in range(1, n + 1):
    for row in range(i + 2): 
        print(' ' * (n + 2 - row) + '*' * (2 * row + 1))

for _ in range(x):
        print(' ' * (n + 1) + '#' * y)