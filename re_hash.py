import random
import hashlib
from collections import deque
import time
import copy

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


matrix = genMat()
matrix.sort()
print(matrix)

#  Бинарный поиск

def findBinarySearch(matrix, val):
    m = len(matrix) // 2
    i = 0
    j = len(matrix) - 1
    while matrix[m] != val and i <= j:
        if val > matrix[m]:
            i = m + 1
        else:
            j = m - 1
        m = (i + j) // 2
    if i > j:
        print("Искомого числа в массиве нет")
    else:
        print("Индекс: ", m)


print("Бинарный поиск")
print("Введите элемент, который хотите найти: ")
while True:
    try:
        element_1 = int(input("Введите элемент который хотите найти "))
    except:
        print("Ошибка, введено не целое число")
        continue
    break
mas_bin = matrix
start = time.time()
findBinarySearch(mas_bin, element_1)
end = time.time() - start

print("Время затраченное на поиск: ",'%.16f' % end)


class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
            else:
                self.data = data

    def findval(self, lkpval):
        if lkpval < self.data:
            if self.left is None:
                print(lkpval, "не найден.")
                return False
            return self.left.findval(lkpval)
        elif lkpval > self.data:
            if self.right is None:
                print(lkpval, "не найден.")
                return False
            return self.right.findval(lkpval)
        else:
            print(self.data, 'найден.')
            return True

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()


def make_a_tree(arr):
    root = Node(arr[0])
    for i in arr[1::]:
        root.insert(i)
        return root

print("Бинарное деререво")
mas_tree = matrix
root = make_a_tree(mas_tree)
num = int(input("Введите элемент, который хотите найти: "))
start = time.time()
result = root.findval(num)
end = time.time() - start
print("Время затраченное на поиск: ", end)


#  Фибонначиев поиск
def fibonacciSearch(matrix, val):
    fibfirst = 0
    fibsecond = 1
    fibthird = fibfirst + fibsecond
    while fibthird < len(matrix):
        fibfirst = fibsecond
        fibsecond = fibthird
        fibthird = fibfirst + fibsecond
    index = -1
    while fibthird > 1:
        i = min(index + fibfirst, len(matrix) - 1)
        if matrix[i] < val:
            fibthird = fibsecond
            fibsecond = fibthird
            fibthird = fibthird - fibsecond
            index = i
        elif matrix[i] > val:
            fibthird = fibfirst
            fibsecond = fibsecond - fibfirst
            fibfirst = fibthird - fibsecond
        else:
            return i
    if fibsecond and matrix[index + 1] == val and index < len(matrix) - 1:
        return index + 1
    return -1
print("Фибоначчиев поиск")
print("Введите элемент, который хотите найти: ")
while True:
    try:
        element_2 = int(input("Введите элемент который хотите найти "))
    except:
        print("Ошибка, введено не целое число")
        continue
    break
mas_fib = matrix
start = time.time()
a = fibonacciSearch(matrix, element_2)
end = time.time() - start
if a == -1:
    print("Искомого числа в массиве нет")
else:
    print("Индекс: ", a)
    print("Время затраченное на поиск: ", end)


#  Интерполяционный поиск
def interpolationSearch(lst, val):
    low = 0
    high = (len(lst) - 1)
    while (low <= high) and (val >= lst[low]) and (val <= lst[high]):
        index = low + int((((high - low) / (lst[high] - lst[low])) * (val - lst[low])))
        if lst[index] == val:
            return index
        if lst[index] < val:
            low = index + 1
        if lst[index] > val:
            high = index - 1
    return -1
print("Интерполяционный поиск")
print("Введите элемент, который хотите найти: ")
while True:
    try:
        element_3 = int(input("Введите элемент который хотите найти "))
    except:
        print("Ошибка, введено не целое число")
        continue
    break
mas_inter = copy.deepcopy(matrix)
start_time_inter = time.time()
b = interpolationSearch(mas_inter, element_3)
end_time_inter = time.time()-start_time_inter
if b == -1:
        print("Искомого числа в массиве нет")
else:
        print("Индекс: ", b)
        print("Время работы: ", end_time_inter)

# Простое рехэширование
def simple_re_hash(sl, matrix):
    for j in range(0, len(matrix)):
        temp = str(matrix[j])
        i = 1
        while True:
            if hash(temp) not in sl.keys():
                sl[hash(temp)] = matrix[j]
                break
            else:
                while hash(temp) + i in sl.keys():
                    i += 1
                sl[hash(str(matrix[j] + i))] = matrix[j]
                break


# Рехэширование с помощью псевдослучайных чисел
def rand_re_hash(sl, matrix):
    for j in range(0, len(matrix)):
        temp = str(matrix[j])
        while True:
            if hash(temp) not in sl.keys():
                sl[hash(temp)] = matrix[j]
                break
            else:
                temp = str(matrix[j] + (random.randint(0, 1000)))

def chain_method(sl, matrix):
    for j in range(0, len(matrix)):
        temp = str(matrix[j])
        if hash(temp) in sl.keys():
            if isinstance(sl[hash(temp)], deque):
                sl[hash(temp)].append(matrix[j])
            else:
                a = sl[hash(temp)]
                sl[hash(temp)] = deque([a, matrix[j]])
        else:
            sl[hash(temp)] = matrix[j]


print("Метод простого рехеширования")
slsimple = dict()
simple_re_hash(slsimple, matrix)
stroksimple = str(slsimple.items())
print(stroksimple)
print("Метод простого рехеширования с использованием псевдослучайных чисел")
slrand = dict()
rand_re_hash(slrand, matrix)
strokrand = str(slrand.items())
print(strokrand)
print("Метод рехеширования с использованием цепочек")
slrchain = dict()
chain_method(slrchain, matrix)
strokchain = str(slrchain.items())
print(strokchain)
