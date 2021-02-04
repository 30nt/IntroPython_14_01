# my_set = set("qwerty")
# print(my_set)
# my_set.remove("a")  Будет ошибка
# my_set.discard("a") Ничего не будет
# print(my_set)

# Словари, методы словарей

# ascii_table = {number: chr(number) for number in range(ord("a"), ord("z") + 1)}
# print(ascii_table)

key = "a"
# if key in ascii_table: # in проверяет ключи а не значения
#     print(ascii_table[key])

# result = ascii_table[key]
# print(result)

# result = ascii_table.get(key)
# print(result.upper())

# test_dict = {100: "100", "100": -1, 122: "test"}

# for key in ascii_table: # for идет по ключам а не значениям
#     print(key, ascii_table[key])
#
# for key, value in ascii_table.items():
#     print(key, value)

#
# ascii_table_keys = set(ascii_table.keys())
# # print(type(ascii_table_keys), ascii_table_keys)
#
# test_dict_keys = set(test_dict.keys())
#
# for key in ascii_table_keys.intersection(test_dict_keys):
#     print(key)
#
# ascii_table_values = ascii_table.values()
# print(ascii_table_values)

# dict_1 = test_dict.copy()
# print(dict_1)
# dict_1[100] = "value"
# print(dict_1)
# print(test_dict)

test_dict = {100: "test", "100": -1, 122: "test"}
new_dict = {"100": 100, -1: "100", "test": 122}
# my_dict = test_dict.update(new_dict)
# print(my_dict)
# print(test_dict)

my_dict = {}
my_dict.update(test_dict)
my_dict.update(new_dict)
print(my_dict)

my_dict = {**test_dict, **new_dict}
print(my_dict)



# new_dict = {value: key for key, value in test_dict.items()}
# print(new_dict)

# values = list(test_dict.values())
# result = len(values) == len(set(values))
# print(result)