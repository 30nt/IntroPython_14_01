import random as rnd


def create_random_point():
    point = (rnd.randint(-10, 10),
             rnd.randint(-10, 10),
             rnd.randint(-10, 10))
    return point

def print_point(point):
    for key, value in point.items():
        print(f"Name: {key}, point: {value}")

# value = random.randint(1,10)
# print(value)

# from random import *

# value = random.randint(1,10)
# print(value)
#
# value_2 = random.choice("qwerty")
# print(value_2)
#
# test_list = [1,2,3]
# random.shuffle(test_list)
# print(test_list)

point_a = {"A": create_random_point()}
point_b = {"B": create_random_point()}

print_point(point_a)
