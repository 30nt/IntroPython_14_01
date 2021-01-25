# методы строк
my_string_1 = 'qwerty'
my_string_2 = "qwerty"
my_string_3 = '''qwerty'''
my_string_4 = """qwerty"""
my_spec_case = 'ООО "Рога и копыта"'
my_spec_case = "Bill's table"
my_spec_case = '''Bill's table ООО "Рога и копыта"'''
print(my_spec_case)
value = 10/3
my_value = f"value: {value} ------>>>> {my_spec_case}"
print(my_value)
print("value: {:.2f}".format(value))

my_string_1 = 'q\nwer\ty'
print(my_string_1)
my_path = r"C:\\tmp\new.txt"
print(my_path)

my_string_1 = 'qqwe qr dtysfdk Tjgakl'
index = 76
print(len(my_string_1))
if -len(my_string_1) <= index < len(my_string_1):
    print(my_string_1[index])

# my_string_1[0] = "Q"  # вставка сивола не работает

print(my_string_1[4:18])
print(my_string_1[4:-3])
print(my_string_1[10:200])
print(my_string_1[10:])
print(my_string_1[:10])

print(my_string_1[::2])  # символы на четных местах в строке
print(my_string_1[1::2])  # символы на нечетных местах в строке
print(my_string_1[::-1]) # строка в обратном порядке

print(my_string_1[8:2:-1]) # Лучше так не делать. Явное лучше неявного
new_str = my_string_1[3:9]
new_str = new_str[::-1]
print(new_str)

new_str = "Q" + my_string_1[1:]
new_str = f"Q{my_string_1[1:]}"
print(new_str)

first_simbol = my_string_1[0]
big_first_symbol = first_simbol.upper()
new_str = my_string_1.replace(first_simbol, big_first_symbol, 1)
print(new_str)

new_str = my_string_1.capitalize()
print(new_str)

new_str_2 = new_str.replace("D", "", 3)
print(new_str_2)

# цикл for

for symbol in my_string_1:
    if symbol not in 'eyuioa' and symbol.islower():
        print(f"symbol: {symbol}")



# тернарный оператор
value = input("Введи целое число")
if value.isdigit():
    value = int(value)
    if not value % 5:
        result = value * 2
    else:
        result = 0
    print(result)

    # результат = выражение_если_да if условие else выражение_если_нет

    result = value * 2 if not value % 5 else 0
    print(result)