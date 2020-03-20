import numpy as np
while True:
    while True:
        try:
            n, m = 3,3      #задаем размерность матрицы
            a = np.zeros((n, m), dtype=int)     #выделяем место для массива
            b = np.zeros((m, n), dtype=int)     #выделяем место для массива
            break
        except ValueError:          #проверка на ошибки (вводить можно только цифры)
            print('Only nums')

    for i in range(n):
        for j in range(m):
            a[i,j]=int(input(f'A[{i},{j}]='))       #задается значение матрицы пользователем
    print(f'Your matrix: \n {a}')

    for i in range(n):
        for j in range(m):          #произведение транспонирования матрицы
            new = a[j, i]
            b[i, j] = new
    print(f'Your new matrix: \n {b}')
    result = input('Do you want to retry.If yes enter 1 if no something else')
    if result == '1':   #перезапуск программы по нажатию
        continue
    else:
        break