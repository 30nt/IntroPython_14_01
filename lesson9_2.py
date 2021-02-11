# работа с файлами
# json
import os
import json

data = {"test_list": [1, 2, 3, 4, 5], "new": {"qwerty": 11, "foo": "мама"}}

# print(type(json.dumps(data)))

filename = "test_json_write.json"
with open(filename, "w") as js_file:
    json.dump(data, js_file, indent=2)


filename = "test_json.json"
with open(filename, "r") as js_file:
    data = json.load(js_file)
print(data, type(data))

# test_str = '{"name": "John", "age": "24"}'
# test_json = json.loads(test_str)
# print(test_json)

# def read_txt(file_path):
#     with open(file_path, "r") as txt_file:
#         data = []
#         for line in txt_file.readlines():
#             data.append(line)
#     return data
#
#
# def write_txt(file_path, data):
#     with open(file_path, "w") as txt_file:
#         txt_file.writelines(data)
#
#
# path = "Homeworks"
#
# # files = [file for file  in os.listdir(path) if os.path.isfile(os.path.join(path, file))]
# # for file in sorted(files):
# #     # file_path = f"{path}/{file}"
# #     file_path = os.path.join(path, file)
# #     data = read_txt(file_path)
# #     print(data)
#
# data = read_txt("lesson3.py")
# print(data)
# data.append("\n# TEST file write\n")
# write_txt("lesson3.py", data)
