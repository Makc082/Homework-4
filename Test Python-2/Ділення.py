x = int(input("Введіть ціле значення: "))

for y in range(1, x):
    if x % y == 0:
        print(f"Числа на які ділится: {y}")