# lst = [1, 2, 3, 14, 15, 12, 7, 6]
# func = lambda x: x * 2
# new_list = []
#
# for item in lst:
#     new_list.append(func(item))
# print(new_list)


# def fun1(x):
#     return x * 2
# print(fun1(3))

# fun = lambda y: y * 2

# print(fun(2))
# lst = [1, 2, 3, 14, 15, 12, 7, 6]
# new_list = []
# func = lambda num: num / 2
#
# for item in lst:
#     new_list.append(func(item))
# print(new_list)
#
# gen_list = [func(elem) for elem in lst]
# print(gen_list)

# lst = [1, 2, 3, 14, 13, 12, 15]

# f1 = lambda b: b * 2
# nums = map(f1, lst)
# print(list(nums))

# nums = list(map(lambda b: b * 2, lst))
# print(nums)

# cubes = list(map(lambda x: x ** 3, range(1, 16)))
# print(cubes)

# lst = [1, 2, 4, 56, 2, 1, 27, 24, 12, 18, 23, 14, 356, 13, 132]
# new_list = []

# func1 = lambda x: x % 2 == 0
# for item in lst:
#     if func1(item):
#         new_list.append(item)
#
# print(new_list)

# list_1 = filter(func1, lst)
# print(list(list_1))

# print(list(filter(lambda x: x % 2 == 0, lst)))

# nums = list(filter(lambda x: x % 3 == 0, lst))
# print(nums)
# def number oladi va numbergacha bolgan sonlani 2, 3, 5, 7, 9 filtrlab javobini dict chiqaradi

### {"2ga": [2, 4...],
#    "3ga": [3, 6...], ...}

#### Dekarator
import time


# def get_big_int(*args, **kwargs):
#     res = 1
#     for arg in args:
#         res += arg ** 50000
#     return len(str(res))

def get_working_time(function):
    def inner_function(*args, **kwargs):
        started_at = time.time()
        result = function(*args, **kwargs)
        ended_at = time.time()
        working_time = ended_at - started_at
        print(f"Funktsiyamiz {working_time} sekundda tugadi")
        return result
    return inner_function

# new_func = get_working_time(get_big_int)
# result = new_func(1000, 2000, 3000)
@get_working_time
def get_big_int(*args, **kwargs):
    res = 1
    for arg in args:
        res += arg ** 50000
    return len(str(res))

get_big_int(1000, 2000, 50000)