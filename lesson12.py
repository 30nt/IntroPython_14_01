import requests

url = "http://api.forismatic.com/api/1.0/"

for number in range(1, 20):
    params = {"method": "getQuote",
              "format": "json",
              "key": number,
              "lang": "ru"}
    responce = requests.get(url, params=params)
    result = responce.json()
    for key in result:
        print(f"{key} ------ {result[key]}")

















# my_list_1 = [1,2,3,4]
# my_list_2 = [10, 20, 30]
# my_list_3 = [5,6,7]
# test = list(zip(my_list_1, my_list_2, my_list_3))
# print(test)