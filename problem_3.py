import random
def genMat():
    while True:
        try:
            m = int(input("Введите кол-во столбцов в матрице: "))
        except:
            print("Ошибка, введено не целое число")
            continue
        break
    while True:
        try:
            n = int(input("Введите кол-во строк в матрице: "))
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
    matrix = [[random.randint(min_limit, max_limit) for j in range(m)] for i in range (n)]
    return(matrix)


matrix = genMat()
print(matrix)


def sortDioMat(matrix):
    stroke = len(matrix)
    raw = len(matrix[0])
    for i in range(2, raw):
        first_stroke = 1
        while first_stroke != 0:
            if matrix[first_stroke][i] < matrix[first_stroke - 1][i - 1]:
                matrix[first_stroke][i], matrix[first_stroke - 1][i - 1] = matrix[first_stroke - 1][i - 1], matrix[first_stroke][i]
                i -= 1
                first_stroke -= 1
            else:
                first_stroke += 1
            if first_stroke == i:
                break
    for k in range(2, stroke):
        first_raw = 1
        while first_raw != 0:
            if matrix[k][first_raw] < matrix[k - 1][first_raw - 1]:
                matrix[k][first_raw], matrix[k - 1][first_raw - 1] = matrix[k - 1][first_raw - 1], matrix[k][first_raw]
                k -= 1
                first_raw -= 1
            else:
                first_raw += 1
            if first_raw == k:
                break

def sortDioMatGreat(matrix):
    stroke = len(matrix)
    raw = len(matrix[0])
    for p in range(0, stroke):
        for i in range(raw - 1):
            for j in range(stroke - 1):
                if matrix[j][i] > matrix[j + 1][i + 1]:
                    matrix[j][i], matrix[j + 1][i + 1] = matrix[j + 1][i + 1], matrix[j][i]
    return matrix

#        first_stroke = 0
 #       while first_stroke < (stroke - 1):
  #          while matrix[first_stroke][i] > matrix[first_stroke + 1][i + 1] and i >= 0 and first_stroke >= 0:
   #             matrix[first_stroke][i], matrix[first_stroke + 1][i + 1] = matrix[first_stroke + 1][i + 1], matrix[first_stroke][i]
    #            first_stroke -= 1
     #           i -= 1
      #      first_stroke += 1


sortDioMatGreat(matrix)


def printMatrix(matrix):
   for row in matrix:
      for x in row:
          print ( "{:4d}".format(x), end = "" )
      print ()


printMatrix(matrix)