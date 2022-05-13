# Реализовать методы поиска подстроки в строке. Добавить возможность ввода строки и подстроки с клавиатуры.
# Предусмотреть возможность существования пробела. Реализовать возможность выбора опции чувствительности или нечувствительности к
# регистру. Оценить время работы каждого алгоритма поиска и сравнить его со временем работы стандартной функции поиска,
# используемой в выбранном языке программирования.

# Упрощённый алгоритм Бойера-Мура

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
if buffer == 'да' or buffer =='Да':
    is_case_sensitive = True


def build_table(s):
    dic_table = dict()
    length = len(s)
    for i in range(length - 1):
        dic_table[s[i]] = length - i - 1
        if not s[length - 1] in dic_table:
            dic_table[s[length - 1]] = length
    return dic_table


def boyer_mur_search(s_main, s_sought, case_sensitive = True):
    if not case_sensitive:
        s_main = s_main.lower()
        s_sought = s_sought.lower()

    dic_table = build_table(s_sought)
    s_sought_len = len(s_sought)
    current_step = s_sought_len - 1

    while current_step < len(s_main): # основной цикл для поиска подстроки
        s_sought_i = s_sought_len - 1 # индекс для подстроки
        for i in range(current_step, current_step - s_sought_len, -1):
            if s_main[i] != s_sought[s_sought_i]: # слово не совпало. Указываем необходимый шаг и выходим из for
                if s_main[i] in dic_table:
                    step = dic_table[s_main[i]]
                else:
                    step = s_sought_len
                    break

        if i == current_step - s_sought_len + 1: # последняя итерация for. Все символы совпали, возвращаем индекс
            return i
        s_sought_i -= 1

        current_step += step # двигаем место поиска на шаг



print(boyer_mur_search(main_string, string_to_find, case_sensitive = is_case_sensitive), "- Номер элемента с чувствительностью регистра")
print(boyer_mur_search(main_string, string_to_find, case_sensitive = False), "- Номер элемента без чувствительности")

print("Упрощённый алгоритм Бойера-Мура: " + str(timeit.timeit("boyer_mur_search(main_string, string_to_find, case_sensitive=is_case_sensitive)", number = 1, globals = globals())))
print("Поиск по умолчанию: " + str(timeit.timeit("main_string.find(string_to_find)", number = 1, globals = globals())))