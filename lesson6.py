my_list_1 = [10,20,30,40,50, 60]
my_list_2 = [1,2,3,4,5,6,7,8,9,0]
my_result = []

len_my_list_1 = len(my_list_1)
len_my_list_2 = len(my_list_2)
min_len_lists = min(len_my_list_1, len_my_list_2)
last_part = my_list_2[min_len_lists:] if len_my_list_2 > len_my_list_1 else my_list_1[min_len_lists:]

for index in range(min_len_lists):
    my_result.append(my_list_1[index])
    my_result.append(my_list_2[index])
my_result.extend(last_part)

print(my_result)

##########################################################
# """
# Цикл с условием(while)
# Игра с угадыванием числа.
# """
from random import randint
min_number = 1
max_number = 10
goal = randint(min_number, max_number)

value = int(input(f"Угадай число в диапазоне от {min_number} до {max_number}"))
value_is_goal = False

while not value_is_goal:
    if value > goal:
        value = int(input(f"Попробуй число меньше"))
    elif value < goal:
        value = int(input(f"Попробуй число больше"))
    else:
        value_is_goal = True
#
# print(f"Угадал!!!!")

# while value != goal:
#     if value > goal:
#         value = int(input(f"Попробуй число меньше"))
#     else:
#         value = int(input(f"Попробуй число больше"))

# while True:
#     if value > goal:
#         value = int(input(f"Попробуй число меньше"))
#     elif value < goal:
#         value = int(input(f"Попробуй число больше"))
#     else:
#         break


##########################################################

# split, join

test_str = "Qwerty is                  first sample"
result = test_str.split()
print(result)
result = "___".join(result)
print(result)

##########################################################


alphabet = []
for index in range(ord("A"), ord('Z') + 1):
    alphabet.append(chr(index))

alphabet = [chr(index) for index in range(ord("a"), ord('z') + 1)]
alphabet = "".join((alphabet))
print(alphabet)

test_list = ["qwe", 'asd', 'zxc', 'ert']
print(test_list)

[print(value) for value in test_list]

test_list = ["qwe", 'asd', 'zxc', 'ert', 3, 5, '12']
int_list = [int(value) for value in test_list if type(value) == int or value.isdigit()]
print(int_list)

test_list = [12,45,670,123]
int_list = [value for value in test_list if value > 100]
print(int_list)

# Множества set
my_list = [1, 2, 3, "12", "3", 2, 234, 12, 3, 2, 1, 1]
my_set = set(my_list)
print(my_set, type(my_set))

my_str_1 = "wfgasdvkzhvkjhfjdgajsdfgkcn<kjskuqq"
my_str_2 = "qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqaysfdjagsc<ncl<a"

my_set_1 = set(my_str_1)
my_set_2  = set(my_str_2)
result_set = my_set_1.union(my_set_2)
print(result_set)

new_list = list(set(my_str_1))
print(len(new_list))
for symbol in set(my_str_1):
    print(f"Symbol: {symbol} --> {my_str_1.count(symbol)}")

##########################################################

# Словарь dict  ключ:значение
my_dict = {"a": 97,
           "b": 98,
           "c": 99,
           "z": ord("z"),
           121: print,
           "qwerty": my_set_1,
           (1,("q")): "test"}
print(my_dict)
person = {"name": "John",
          "age": 32,
          "e-mail": "test@gmali.com",
          "address": {"city": "Dnipro",
                      "zip": "49000"}}

print(person["address"]["city"])


##########################################################
# Консультация
my_string = '0123456789'
result = []
for symb_1 in my_string:
    for symb_2 in my_string:
        value = int(symb_1 + symb_2)
        result.append(value)
print(result)


for index in range(5):
    print(my_string[index * 2: index * 2 + 2])