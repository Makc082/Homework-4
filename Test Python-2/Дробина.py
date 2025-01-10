import os
os.system("cls")

star = int(input("Введітькількість зірочок: "))
lines = int(input("Ведіть кількість дробинок: ")) 
tab = "\t"

for step in range(lines):
    print(f"{tab * step} {'*' * star}\n\n", end="")