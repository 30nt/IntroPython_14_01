# подключение нескольких файлов в проект
# csv
from tools import read_csv

filename = "test2.csv"
data = read_csv(filename)

assert len(data[0]) > 1, "One column!!!"




# from tools import read_csv, write_csv
#
# filename = "test.csv"
# data = read_csv(filename)
# print(data)
# write_csv("test2.csv", data)
# with open(filename, 'r', encoding="utf-8") as csv_file:
#     data = []
#     reader = csv.DictReader(csv_file)
#     for row in reader:
#         data.append(dict(row))
#
# print(data)
#
# data.append({'Name': 'Tod', 'Age': '30', 'Value': '12.4', 'Text': 'qwerty'})
#
# with open(filename, 'w', encoding="utf-8") as csv_file:
#     fieldnames = data[0].keys()
#     writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
#     writer.writeheader()
#     writer.writerows(data)

# data = read_csv(filename)
#
# # data.append(["Jack", 45, 10.0])
# data[0].append("Text")
# for row in data[1:]:
#     row.append("test")
#
# write_csv(filename, data)


# ДЗ
#
# def write_txt(filename, data):
#     pass
#
# def write_file(filename, data):
#     extension = filename.rsplit(".", 1)[-1]
#     if extension == "txt":
#         write_txt(filename, data)
#
#
#
# write_file("data.txt", "uqwgeuafasvzv")
# write_file("data.json", {"name": "John"})
# write_file("data.csv", [[1, 2, 3], [4, 5, 6]])


