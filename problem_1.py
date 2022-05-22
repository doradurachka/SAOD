import random

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
    return(matrix)

def quickSort(matrix):
    for i in range(len(matrix)):
        qquickSort(0, len(matrix) - 1, matrix)
    return matrix


def qquickSort(_first, _last, matrix):
    first = int(_first)
    last = int(_last)
    middle = int((first + last) / 2)

    while (first < last):

        while (matrix[first] < matrix[middle]):
            first += 1
        while (matrix[last] > matrix[middle]):
            last -= 1
        if (first <= last):
           matrix[first], matrix[last] = matrix[last], matrix[first]
           first += 1
           last -= 1

        if (_first < last):
            qquickSort(_first, last, matrix)
        if (first < _last):
            qquickSort(first, _last, matrix)


def triangle(matrix):
    a = matrix[0]
    b = matrix[1]
    c = matrix[2]
    p = 0
    n = 1
    for i in range(len(matrix)):
        # if matrix[i - 1] + matrix[i] > matrix[i + 1] and matrix[i - 1] + matrix[i + 1] > matrix[i] and matrix[i + 1] + matrix[i] > matrix[i - 1]:
            # p = matrix[i] + matrix[i + 1] + matrix[i - 1]
            # print(p)
            # break
        if a + b > c and a + c > b and c + b > a:
            p = a + b + c
            print(p)
            break
        else:
            if n + 3 > len(matrix):
                print(p)
                break
            a = matrix[0 + n]
            b = matrix[1 + n]
            c = matrix[2 + n]
            n += 1


matrix = genMat()
print(matrix)
quickSort(matrix)
print(matrix)
matrix.reverse()
print(matrix)
triangle(matrix)

