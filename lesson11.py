import re

# test_str = "qwe123 !@#$%^sdg  712653725721.123 "
# reg_exp = r"[0-9]+"
# result = re.findall(reg_exp, test_str)
# print(result)

numb_list = [1, 2, 3, -2, -10]
str_list = ['a1sd', 'abd', 'zxc', 'q', 'we', 'ASD', "1"]
dict_list = [
    {"name": "John", "age": "1900-1966BC"},
    {"name": "Bob", "age": "1923 - 1958"},
    {"name": "Jacob", "age": "1845- 1899"}
]

def sort_key_by_name(sort_dict):
    value = sort_dict["name"]
    return value


def sort_key_by_len_name(sort_dict):
    return len(sort_dict["name"])

def sort_by_bday(sort_dict):
    age = sort_dict["age"]
    years = re.findall(r'[0-9]+', age)
    return int(years[0])

result = sorted(dict_list, key=sort_by_bday)
print(result)







# 1. Создать папку ./alphabet/ или проверить, что папка существует.
# 2. В папку ./alphabet/ поместить файлы вида a.txt, b.txt, ..., z.txt в которых
# будет записана строка алфавита, но с заменой буквы из названия файла на прописную.
# Пример: для b.txt строка будет aBcde...
# 3. Сделать щелчек Таноса - удалить случайным образом половину всех файлов в этой папке.
import os
import string


def create_dir(dir_name):
    if not os.path.isdir(dir_name):
        os.mkdir(dir_name)
    # try:
    #     os.mkdir(dir_name)
    # except FileExistsError:
    #     pass


def create_file(symbol, dir_name):
    # filename = f"{dir_name}/{symbol}.txt" # C:\\tmp\test\alphabet   идея не очень ))
    filename = os.path.join(dir_name, f"{symbol}.txt")
    with open(filename, "w") as file:
        file.write(string.ascii_lowercase.replace(symbol, symbol.upper()))


def create_all_files(dir_name):
    for symbol in string.ascii_lowercase:
        create_file(symbol, dir_name)


def tanos_click(dir_name):
    files = list(set(os.listdir(dir_name)))
    for file in files[:len(files) // 2]:
        os.remove(os.path.join(dir_name, file))


folder = "alphabet"
# create_dir(folder)
create_all_files(folder)
tanos_click(folder)
