import random


def random_num():
    a = range(0, 10)
    b = random.sample(a, 6)
    c = ""
    for i in b:
        c += str(i)
    return c

random_num()
