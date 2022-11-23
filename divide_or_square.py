import math


def divide_or_square(a):
    return round(math.sqrt(a), 2) if a % 5 == 0 else a % 5


print(divide_or_square(10))
