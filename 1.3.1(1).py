import numpy as np
while True:
    while True:
        try:
            n = int(input('Enter amount of digits'))  #задаем введение количества цифр
            a = np.zeros((n), dtype=int)    #выделяем место для массива
            b = np.zeros((n), dtype=int)    #выделяем место для массива
            break
        except ValueError:   #проверка на ошибки (вводить можно только цифры)
            print('Only nums')

    for i in range(n):
        a[i] = int(input('Enter your digits: '))    #ввод цифр
    print(a)

    for i in range(n):
        b[i] = a[n - 1 - i]     #вывод значения в обратном порядке
    print(f'New array:{b}')
    result = input('Do you want to retry.If yes enter 1 if no something else')
    if result == '1':
        continue
    else:
        break