n = int(input("Введите размер матрицы: "))
bacterie_array = []

for i in range(n):
    bacterie_array.append([])
    for j in range(n):
        bacterie_array[i].append(int(input("Введите значение: ")))
print(bacterie_array)

k = int(input("Введите количество капель антибиотика: "))
for i in range(k):
    x_coord = int(input("Введите координату по x: "))
    y_coord = int(input("Введите координату по y: "))

    if bacterie_array[x_coord][y_coord] < 8:
        bacterie_array[x_coord][y_coord] = 0
    else:
        bacterie_array[x_coord][y_coord] -= 8
    if x_coord > 0:
        if bacterie_array[x_coord - 1][y_coord] >= 4:
            bacterie_array[x_coord - 1][y_coord] -= 4
        else:
            bacterie_array[x_coord - 1][y_coord] = 0
        if y_coord > 0:
            if bacterie_array[x_coord - 1][y_coord - 1] >= 4:
                bacterie_array[x_coord - 1][y_coord - 1] -= 4
            else:
                bacterie_array[x_coord - 1][y_coord - 1] = 0
        if y_coord < (n - 1):
            if bacterie_array[x_coord - 1][y_coord + 1] >= 4:
                bacterie_array[x_coord - 1][y_coord + 1] -= 4
            else:
                bacterie_array[x_coord - 1][y_coord + 1] = 0

    if x_coord < (n - 1):
        if bacterie_array[x_coord + 1][y_coord] >= 4:
            bacterie_array[x_coord + 1][y_coord] -= 4
        else:
            bacterie_array[x_coord + 1][y_coord] = 0
        if y_coord > 0:
            if bacterie_array[x_coord + 1][y_coord - 1] >= 4:
                bacterie_array[x_coord + 1][y_coord - 1] -= 4
            else:
                bacterie_array[x_coord + 1][y_coord - 1] = 0
        if y_coord < (n - 1):
            if bacterie_array[x_coord + 1][y_coord + 1] >= 4:
                bacterie_array[x_coord + 1][y_coord + 1] -= 4
            else:
                bacterie_array[x_coord + 1][y_coord + 1] = 0

    if y_coord > 0:
        if bacterie_array[x_coord][y_coord - 1] >= 4:
            bacterie_array[x_coord][y_coord - 1] -= 4
        else:
            bacterie_array[x_coord][y_coord - 1] = 0

    if y_coord < n - 1:
        if bacterie_array[x_coord][y_coord + 1] >= 4:
            bacterie_array[x_coord][y_coord + 1] -= 4
        else:
            bacterie_array[x_coord][y_coord + 1] = 0

for i in range(n):
    for j in range(n):
        print(bacterie_array[j][i], end=' ')
    print(" ")
