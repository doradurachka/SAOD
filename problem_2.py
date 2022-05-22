import random

# генерация рандомного массива
def genMat():
    while True:
        try:
            m = int(input("Введите кол-во элементов в матрице: "))
        except:
            print("Ошибка, введено не целое число")
            continue
        break
    while True:
        try:
            min_limit = int(input("Введите минимальное значение в матрице: "))
        except:
            print("Ошибка, введено не целое число")
            continue
        break
    while True:
        try:
            max_limit = int(input("Введите максимальное значение в матрице: "))
        except:
            print("Ошибка, введено не целое число")
            continue
        break
    if min_limit > max_limit:
        min_limit = -250
        max_limit = 1012
    matrix = [random.randint(min_limit, max_limit) for j in range(m)]
    return (matrix)

# создание массива
matrix = genMat()
print(matrix)

# функция сортировки массива для формирования максимального числа
def sortMaxnumber(matrix):
    k = 0 # с этим работает без этого нет
    for i in range(len(matrix)):
        while i > 0:
            n = 1
            d = 1
            p = matrix[i - 1] % 10 # выбор последней цифры в числе
            g = matrix[i] % 10 # выбор последней цифры в числе
            while (matrix[i - 1] // (pow(10, n))) > 0: # выбор первой цифры в числе
                p = matrix[i - 1] // (pow(10, n - k))
                n += 1
            while (matrix[i] // (pow(10, d))) > 0: # выбор первой цифры в числе
                g = matrix[i] // (pow(10, d - k))
                d += 1
            if g > p: # перенос большего числа влево
                matrix[i - 1], matrix[i] = matrix[i], matrix[i - 1]
                i -= 1
                print(n, d)
                print(matrix)
        k += 1 # с этим работает без этого нет
        print(k)


def sortMaxnumberSoft(matrix):
    for i in range(len(matrix)):
        while i > 0:
            n = 1
            d = 1
            p = matrix[i - 1] % 10  # выбор последней цифры в числе
            g = matrix[i] % 10  # выбор последней цифры в числе
            if matrix[i] == matrix[i - 1]:  # чтобы не зацикливалось
                break
            while (matrix[i - 1] // (pow(10, n))) != 0:  # выбор первой цифры в числе
                p = matrix[i - 1] // (pow(10, n))
                n += 1
            while (matrix[i] // (pow(10, d))) != 0:  # выбор первой цифры в числе
                g = matrix[i] // (pow(10, d))
                d += 1
            m = 1
            while (g == p):  # сортировка по 2 и далее цифре
                if matrix[i] // pow(10, m) == 0:
                    matrix[i - 1], matrix[i] = matrix[i], matrix[i - 1]
                    break
                if matrix[i - 1] // pow(10, m) == 0:
                    break
                n = 1
                d = 1
                while (matrix[i - 1] // (pow(10, n))) != 0:  # выбор первой цифры в числе
                    p = matrix[i - 1] // (pow(10, n - m))
                    n += 1
                while (matrix[i] // (pow(10, d))) != 0:  # выбор первой цифры в числе
                    g = matrix[i] // (pow(10, d - m))
                    d += 1
                m += 1
            if g > p:  # перенос большего числа влево
                matrix[i - 1], matrix[i] = matrix[i], matrix[i - 1]
            i -= 1


sortMaxnumberSoft(matrix)
print(matrix)
print("".join(map(str, matrix)))
