import os
os.system("cls")

n = int(input("Введіть кількість ярусів: "))

for i in range(1, n + 1):
    for x in range(n - i):
        print(" ", end="")

    for x in range(2 * i - 1 ):
        print("*", end="")
    print()