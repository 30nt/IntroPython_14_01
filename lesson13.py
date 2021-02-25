# Словарик урока:
# Класс
# Экзкмпляр класса (self)
# Атрибут класса
# Атрибут экземпляра класса  <<--
# Метод класса
# Метод экземпляра класса  <<--
import random


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # def __init__(self, min_limit=-10, max_limit=10):
    #     self.x, self.y = self.create_point(min_limit, max_limit)

    def get_distance(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def create_random_point(self, min_limit, max_limit):
        self.x = random.randint(min_limit, max_limit)
        self.y = random.randint(min_limit, max_limit)


    # def __str__(self):
    #     return f"x={self.x}, y={self.y}"

    def __repr__(self):
        return f"({self.x}; {self.y})"

point_d = Point(3, 4)
print(point_d)
point_d.create_random_point(50, 100)
print(point_d)
dist_d = point_d.get_distance()
print(dist_d)
#
# trinagle = {"A": Point(3, 4),
#             "B": Point(-1, 1),
#             "C": Point(50, 100)}
# print(point_d)
# print(trinagle)

# print(trinagle["A"])
# print(trinagle["A"].x, trinagle["A"].y)
# print(trinagle["B"].x, trinagle["B"].y)
# print(trinagle["C"].x, trinagle["C"].y)

















# class Dog:  # Класс
#     name = "---" # Атрибут класса
#     age = 0
#     weight = 0
#     breed = ""
#     image_path = "/path/to/image"
#
# my_dog = Dog()  # Экзкмпляр класса
# my_dog.name = "Ted"  # Атрибут экземпляра класса
# my_dog.age = 1
# my_dog.weight = 18
# my_dog.breed = "French bulldog"
# my_dog.image_path = "ted.png"
# my_dog.award = "Gold"
# print(my_dog.image_path, my_dog.award)
# # print(my_dog.name, my_dog.age, my_dog.breed)
# # print(my_dog)
#
# neighbor_dog = Dog()  # Экзкмпляр класса
# neighbor_dog.name = "Arch"  # Атрибут экземпляра класса
# # print(neighbor_dog.name)
# print(neighbor_dog.image_path)
#
# Dog.image_path = "/new/path/to/image"
# print(my_dog.image_path)
# print(neighbor_dog.image_path, neighbor_dog.award)




