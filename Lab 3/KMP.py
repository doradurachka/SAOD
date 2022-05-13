# Реализовать методы поиска подстроки в строке. Добавить возможность ввода строки и подстроки с клавиатуры.
# Предусмотреть возможность существования пробела. Реализовать возможность выбора опции чувствительности или нечувствительности к
# регистру. Оценить время работы каждого алгоритма поиска и сравнить его со временем работы стандартной функции поиска,
# используемой в выбранном языке программирования.

# Алгоритм Кнута-Морриса-Пратта

import timeit

main_string = 'замок закрыт на большущий ЗАМОК'
string_to_find = 'ЗАМОК'
is_case_sensitive = False

print('Введите основную строку или оставьте пустой для строки по умолчанию: ')
buffer = input()
if buffer != '':
    main_string = buffer
    buffer = ''
else:
    print('По умолчанию: замок закрыт на большущий ЗАМОК')

print('Введите строку для поиска или оставьте пустой для строки по умолчанию: ')
buffer = input()
if buffer != '':
    string_to_find = buffer
    buffer = ''
else:
    print('По умолчанию: ЗАМОК')

print('Должен ли поиск быть чувствительным к регистру?')
buffer = input()
if buffer == 'Да' or buffer == 'да':
    is_case_sensitive = True


def prefix(s):
    str_prefix = [0]*len(s)
    for i in range(1, len(s)):
        k = str_prefix[i-1]
        while k > 0 and s[k] != s[i]:
            k = str_prefix[k-1]
        if s[k] == s[i]:
            k = k + 1
        str_prefix[i] = k
    return str_prefix


def kmp(s_main, s_sought, case_sensitive=True):
    if not case_sensitive:
        s_main = s_main.lower()
        s_sought = s_sought.lower()

    index = -1
    str_prefix = prefix(s_main)
    k = 0
    for i in range(len(s_sought)):
        while k > 0 and s_main[k] != s_sought[i]:
            k = str_prefix[k-1]
        if s_main[k] == s_sought[i]:
            k = k + 1
        if k == len(s_main):
            index = i - len(s_main) + 1
            break
    return index


print(kmp(string_to_find, main_string, is_case_sensitive), "- Номер элемента с чувствительностью регистра")
print(kmp(string_to_find, main_string, False), "- Номер элемента без чувствительности")

# Высчитываем время работы
print("Поиск Кнута-Морриса-Пратта " + str(timeit.timeit("kmp(string_to_find, main_string, is_case_sensitive)", number=1, globals=globals())))
print("Поиск по умолчанию " + str(timeit.timeit("main_string.find(string_to_find)", number=1, globals=globals())))