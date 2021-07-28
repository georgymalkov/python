import random

def func_max(*args):
    el1, el2, el3 = args
    print([el1, el2, el3])
    lst = [el1, el2, el3]
    lst.sort()
    sum_max = lst[1] + lst[2]
    return sum_max

print(func_max(random.randint(0, 100),random.randint(0, 100),random.randint(0, 100)))
