import numpy as np
while True:
    while True:
        try:
            n, m = 3, 3
            a = np.zeros((n, m), dtype=int)     #выделяем место для массива
            b = np.zeros((n, m), dtype=int)     #выделяем место для массива
            c = []
            break
        except ValueError:          #проверка на ошибки (вводить можно только цифры)
            print('Only nums')
    for i in range(n):
        for j in range(m):
            a[i, j] = int(input(f'A[{i},{j}]='))            #задается первая матрица
    print(f'Matrix A: \n{a}')
    for i in range(n):
        for j in range(m):               #задается вторая матрица
            b[i, j] = int(input(f'B[{i},{j}]='))
    print(f'Matrix B: \n{b}')
    c = a*b                     #умножение матриц
    print(f'Multiplication of matrix: \n {c}')
    result = input('Do you want to retry.If yes, enter 1, if no, something else')
    if result == '1':
        continue
    else:
        break