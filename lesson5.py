REVERSE = False

# Except
# value = input("Ввди целое число")
# if value.isdigit():
#     value = int(value)
#     print(value)
# else:
#     print("Надо было ввести целое число")

# try:
#     value = int(value)
#     result = 1 / value
# except (ValueError, ZeroDivisionError):
#     print("Надо было ввести целое число. По умолчанию 1")
#     value = 1
#     result = 1
# # except ZeroDivisionError:
# #     print("На 0 делить нельзя")
# #     value = 0
# #     result = 1
#
# print(result, value)

# my_str = 'blablablacar'
# my_symbol = "bla"
"""
1) У вас есть переменная my_str, тип - str. И переменная my_symbol, тип - str. 
Напечатать ЧИСЛО сколько раз my_symbol встречается в my_str. 
Пример:  my_str="blablacar", my_symbol="bla". 
Вывод на экран:
2
"""
# result = my_str.count(my_symbol)
# print(result)


"""
2) У вас есть переменная my_str, тип - str. И переменная my_symbol, тип - str. 
Напечатать столько раз my_symbol, сколько он встречается в my_str. 
Пример:  my_str="blablacar", my_symbol="bla". 
Вывод на экран:
bla
bla
"""

# for _ in range(my_str.count(my_symbol)):
#     print(my_symbol)
#
#
# result = (my_symbol + "\n") * my_str.count(my_symbol)
# result = result.strip()
# print(result)


"""
3) У вас есть переменная my_str, тип - str. Напечатать ЧИСЛО сколько 
РАЗНЫХ символов встречается в my_str. 
Большая и маленькая буква считается как один символ. 
Пробелы, запятые и т.д. считаем тоже как символы.
Пример:  my_str="bla BLA car". 
Вывод на экран:
6
"""
# my_str="bla BLA car"
#
# my_str = my_str.upper()
# # unique_symbols = []
# unique_symbols = ""
# for symbol in my_str:
#     if symbol not in unique_symbols:
#         # unique_symbols.append(symbol)
#         unique_symbols += symbol
# print(len(unique_symbols), unique_symbols)


"""
4)
Дана строка my_str и пустой список my_list.
Заполнить my_list символами из my_str, 
которые стоят на четных местах в строке (считаем с 0)
"""
# my_list = []
# for index, symbol in enumerate(my_str):
#     if not index % 2:
#         my_list.append(symbol)
# print(my_list)
#
# for symbol in my_str[::2]:
#     my_list.append(symbol)
# print(my_list)


"""
5)
Дана строка my_str, список str_index целых чисел в диапазоне от 
0 до длинны строки минус 1, пустой список my_list.
Заполнить my_list символами из my_str, которые стоят на местах с 
индексами из str_index
"""
# my_str = "test string"
# str_index = [2, 4, 10, 5, 1, 1, 3, 5, 6, 7]
# my_list = []
#
# for index in str_index:
#     value = my_str[index]
#     my_list.append(value)
#     # my_list.append(my_str[index])
#
# print(my_list)



"""
6)
Даны списки my_list_1 и my_list_2.
Создать список my_result в который поместить элементы из my_list_1 и 
my_list_2 через один, начиная с my_list_1.
a) кол-во эл-тов одинаковое
б) кол-во эл-тов разное. Оставшиеся дописать в конец.
"""
# my_list_2 = [1,2,3]
# my_list_1 = [10,20,30,40,50, 60]
# my_result = []
#
# if len(my_list_1) > len(my_list_2):  # Придумать как реализовать правильный порядок в my_result
#     my_list_1, my_list_2 = my_list_2, my_list_1
#
# for index in range(len(my_list_1)):
#     my_result.append(my_list_1[index])
#     my_result.append(my_list_2[index])
# my_result.extend(my_list_2[len(my_list_1):])

# last_common_index = len(my_list_1) - 1
# my_result.extend(my_list_2[last_common_index + 1:])

# print(my_result)



"""
7)
Даны списки my_list_1 и my_list_2.
Создать список my_result в который вначале поместить 
элементы на четных местах из my_list_1, 
а потом все элементы на нечетных местах из my_list_2.
"""

# ДЗ


"""
8)
Дано целое число (int). Определить сколько цифр в этом числе.
"""

my_int = 721364812341234207
# result = len(str(my_int))
# print(result)




"""
9)
Дано целое число. Определить наибольшую цифру в этом числе.
"""

# result = max(str(my_int))
# result = max("123Aa")
# print(result)


"""
10)
Дано целое число. Составить число с цифрами в обратном порядке.
"""

# result = int(str(my_int)[::-1])
# print(result)


"""
11)
Дано целое число. Составить число с цифрами в порядке возрастания(убывания).
"""

result = sorted(list(str(my_int)), reverse=REVERSE)
result = int("".join(result))
print(result, type(result))