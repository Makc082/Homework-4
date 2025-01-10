x = int(input("Введіть ціле число: "))

if x <= 1:
    print(f"Число {x} не є простим.")
else:
    is_prime = True 
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            is_prime = False
            break

    if is_prime:
        print(f"Число {x} є простим.")
    else:
        print(f"Число {x} не є простим.")
