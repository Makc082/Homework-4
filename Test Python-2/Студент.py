n = 2500
m = 3000
s = 0

for i in range(1,11):
    print(f"у місяць {i} студент витрачає: ", round(m,2))
    m = m * 0.05 + m
    s += m
    s = s - n
print("Треба взяти коштів у батьків: ",round(s,2))