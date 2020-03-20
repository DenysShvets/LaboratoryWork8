import numpy as np
while True:
    while True:
        try:
            n, m = 4, 4         #создание матрицы размерностью 4 на 4
            a = np.zeros((n, m), dtype=int)
            b = np.zeros((n, m), dtype=int)
            break
        except ValueError:
            print('Only nums')
    for i in range(n):          #задание значений для первой матрицы
        for j in range(m):
            a[i, j] = int(input(f'A[{i},{j}]='))
            b[i,j] = a[i,j]
            if b[i,j] < 0:
                b[i,j] = 0      #перевод отрицательных значений в нули
    print(f'Your matrix:\n{a}') #вывод матрицы с отрицательными значениями
    print(f'Your new matrix without negative digits\n {b}')  #вывод матрицы с нулями
    result = input('Do you want to retry.If yes enter 1 if no something else')
    if result == '1':
        continue
    else:
        break