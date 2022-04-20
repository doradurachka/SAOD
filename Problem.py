def make_quins_attack(array):
    """
    пересчитывает клетки под атакой на всём поле
    """
    length = len(array)
    for y in range(length):  # очищаем закрытые клетки
        for x in range(length):
            if array[y][x] == 1:
                array[y][x] = 0
    for y in range(length):  # закрываем клетки
        for x in range(length):
            if array[y][x] == 'Q':
                buffer = 0
                for i in range(length):
                    if array[i][x] == 0:  # закрываем клетки по вертикали
                        array[i][x] = 1
                    if array[y][i] == 0:  # закрываем клетки по горизонтали
                        array[y][i] = 1
                    # закрываем клетки по диагонали
                    if x >= y and length > x - y + i >= 0:  # королева в верхней правой части доски
                        if array[i][x - y + i] == 0:
                            array[i][x - y + i] = 1
                    elif length > y - x + i >= 0:  # королева в нижней левой части доски
                        if array[y - x + i][i] == 0:
                            array[y - x + i][i] = 1
                    # закрываем клетки по диагонали
                    if x + y <= length and length > x + y - i >= 0:  # королева в верхней левой части доски
                        if array[i][x + y - i] == 0:
                            array[i][x + y - i] = 1
                    elif length > y + x - i >= 0:  # королева в нижней правой части доски
                        if array[y + x - i][i] == 0:
                            array[y + x - i][i] = 1


def quins(array, quins_amount):
    length = len(array)
    for y in range(length):
        for x in range(length):
            if array[y][x] == 0:  # нашли свободное место для королевы
                array[y][x] = 'Q'
                quins_amount -= 1
                make_quins_attack(array)
                if quins_amount == 0:  # королев не осталось
                    return 1  # королевы успешно расставленны
                if quins(array, quins_amount) == 1:
                    return 1  # королевы успешно расставленны
                else:
                    array[y][x] = 0
                    quins_amount += 1
                    make_quins_attack(array)
    return -1  # неудача


def chess(board_length, quins_amount):
    board = [0] * board_length
    for i in range(board_length):  # формируем нашу доску как массив из массивов
        board[i] = [0] * board_length
    if quins(board, quins_amount) == 1:  # ищем доску
        print("Комбинация найдена!")
    else:
        print("Комбинации не существует!")
    return board


board = chess(8, 8)
def printMatrix(matrix):
   for row in matrix:
      for x in row:
          print (f'{x:>3}', end = "" )
      print ()


printMatrix(board)