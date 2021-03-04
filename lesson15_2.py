# декораторы


# def decorator(function):
#     def wrapper():
#         print("Begin")
#         function()
#         print("End")
#     return wrapper
#
# @decorator
# def spetial_print():
#     print("I am the string!")
#
# spetial_print()

import time


def time_decorator(function):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = function(*args, **kwargs)
        print(time.time() - start_time)
        return result
    return wrapper


@time_decorator
def long_sum(number):
    sum_numbers = 0
    for numb in range(1, number):
        sum_numbers += numb
    return sum_numbers

long_sum(10000000)