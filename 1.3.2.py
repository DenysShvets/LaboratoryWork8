import numpy as np
while True:
    print("Линейный поиск:\n")
    A = np.random.randint(0, 11, 24)
    print("Масив:")
    print(A)
    i = 0
    count = 0
    while i < 24 and A[i] != 11:
        i += 1
        count += 1
    if i == 24:
        print('Элемент', 11, 'Не найден')
        print('Количество сравнений:', count)
    else:
        count += 1
        print('Элемент', 11, 'Впервые встречается в позиции', i)
        print('Количество сравнений:', count)

    A = np.random.randint(0, 8, 24)
    A[-1] = 3
    print("random number array :")
    print(A)
    i = 0
    count = 0
    while i < 24 and A[i] != 3:
        i += 1
        count += 1
    if i == 24:
        print('Элемент', 3, 'Не найден.')
        print('Количество сравнений:', count)
    else:
        count += 1
        print('Item', 3, 'first found in position', i)
        print('Кількість порівнянь:', count)

    print("\nБинарный поиск:\n")
    a = np.random.randint(0, 20, 24)
    A[-1] = 11
    a.sort()
    print("Масив:")
    print(a)
    i = 0
    L = 0
    R = 23
    K = 0
    flag = True

    while L <= R and flag:
        i += 1
        K = (L + R) // 2
        if a[K] == 11:
            print('Элемент', 11, 'Впервые встречается в позиции', K)
            print('Количество сравнений:', i)
            flag = False
        elif a[K] < 11:
            L = K + 1
        elif a[K] > 11:
            R = K - 1
    if flag:
        print('Элемент', 11, 'Не найден.')
        print('Количество сравнений:', i)
    print()

    a = np.random.randint(0, 10, 24)
    a.sort()
    print("Масив:")
    print(a)
    i = 0
    L = 0
    R = 23
    K = 0
    flag = True

    while L <= R and flag:
        i += 1
        K = (L + R) // 2
        if a[K] == 11:
            print('Элемент', 11, 'Впервые встречается в позиции', K)
            print('Количество сравнений:', i)
            flag = False
        elif a[K] < 11:
            L = K + 1
        elif a[K] > 11:
            R = K - 1
    if flag:
        print('Элемент', 11, 'Не найден.')
        print('Количество сравнений:', i)

    print("\nПрямой поиск подряда:\n")
    text = "где то там"
    pattern = "где"
    i = -1
    j = 0
    count = 0
    print('Текст:', text)
    print('Подряд:', pattern)
    while (j < len(pattern)) and i < (len(text) - len(pattern)):
        j = 0
        i += 1
        while j < len(pattern) and pattern[j] == text[i + j]:
            j += 1
            count += 1
    if j == len(pattern):
        print('Подряд не найден в позиции', i)
    else:
        print('Элемент не найден.')
    print('Количество сравнений', count)
    print()
    text = "где то там что то делал"
    pattern = "делал, но забыл"
    i = -1
    j = 0
    count = 0
    print('Текст:', text)
    print('Подряд:', pattern)
    while (j < len(pattern)) and i < (len(text) - len(pattern)):
        j = 0
        i += 1
        while j < len(pattern) and pattern[j] == text[i + j]:
            j += 1
            count += 1
    if j == len(pattern):
        print('Подряд найден в позиции', i)
    else:
        print('Элемент не найден.')
    print('Количество сравнений', count)

    if input('Введите пустой ряд для перезапуска') == '':
        continue
    break