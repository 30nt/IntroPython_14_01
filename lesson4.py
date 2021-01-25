# Кортеж Tuple

my_tuple = (1, 2., 3, "qwerty", True, (1, 2), "qwerty")

print(my_tuple)
print(type(my_tuple))

print(my_tuple[::-1])
print(my_tuple[-1][-1])

for value in my_tuple:
    print(value)

print(my_tuple.count(5))

a = 2
b = 4
tmp = a
a = b
b = tmp
a, b = b, a

tmp = b, a
print(type(tmp), tmp)
a, b = tmp # Распаковка
print(a, b)

my_tuple = (123, "John", "john@gmail.com", 1,  "Qwerty", True, (1, 2))
a_1, a_2, a_3, a_4, a_5, a_6, a_7 = my_tuple

response = (123, "John", "john@gmail.com")
# _, name, _ = response
id, name, e_mail, *values = my_tuple

print(name)

# list Список
print(type(values), values)
print(values[0], values[:-1])

my_list = [1, 2, "asd"]

my_list[0] = "11"
print(my_list)

my_list[0] = my_list[0] * 2
print(my_list)

my_list = [1]
new_list = [my_list] * 6
# new_list = [my_list.copy()] * 6
print(new_list)
my_list[0] = 10
print(my_list)
print(new_list)

my_list.append("Nex element")
print(my_list)
result = []
for value in [1,2,3,4,5]:
    result.append(value ** 2)
# print(result)

new_list = my_list + result
print(new_list)
# my_list.extend(result)
# print(my_list)

last_value = new_list.pop()
print(new_list)
print(last_value)

my_list = [11,21,31,114,51, 34]

for value in my_list:
    print(value ** 2)

for index in range(len(my_list)):
    if not index % 2:
        print(f"{index} -->> {my_list[index]}")

for index, value in enumerate(my_list):
    # print(type(item))
    # index, value = item
    print(f"{index} -->> {value}")

for _ in range(100000):
    print("Hello? World!")