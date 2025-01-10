import os

os.system('cls')

width,heigth = 8, 8

for y in range(heigth):
    for x in range(width):
        if y == 0 or y == heigth - 1 or x == 0 or x == width - 1:
            print("@", end="")
        else:
            print("*", end="")
    print()
input()    
