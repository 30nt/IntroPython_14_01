import random as rnd

DEBUG_MODE = True

def create_point(min_limit: int, max_limit: int, debug_mode: bool = DEBUG_MODE) -> list:
    point = [rnd.randint(min_limit, max_limit),
             rnd.randint(min_limit, max_limit),
             rnd.randint(min_limit, max_limit)]
    if debug_mode:
        print(point)
    return point


min_limit = -100
max_limit = 100
res = create_point(min_limit, max_limit, debug_mode=True)










# def test_variables(*args):
#     args_sum = sum(args)
#     return args_sum

# def test_variables(numb_1, numb_2):
#     return numb_1 ** numb_2
#
#
# def print_number(number, **kwargs):
#     print(kwargs)
#     print(kwargs["value"])
#     print(number)
#
#
# number = 100
# print_number(number=number,
#              string="test",
#              value=200)

# numb_1, numb_2, numb_3 = 10, 34, 12
# result = test_variables(numb_2=numb_2, numb_1=numb_1)
# print(result)

# test_number = 100
# print(test_number)
# result = test_variables(test_number)
# print(result)
# print(test_number)
# print('----------------------')
# number_2 = 23
# res = test_variables(number_2)
# print(res)
