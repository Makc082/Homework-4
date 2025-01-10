start = 0
finish = 10000000

for x in range(start, finish + 1):
    is_prime = True

    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            is_prime = False
            break
    
    if is_prime:
        print(f"Прості числа: {x}")