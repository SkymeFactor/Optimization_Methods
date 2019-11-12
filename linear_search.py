import math

phi = (1.0 + math.sqrt(5)) / 2


def func(x):
    return math.sin(x)

def linear_search(x0, d):
    if func(x0) > func(x0 + d):
        x0 += d
    else:
        if func(x0) > func(x0 - d):
            x0 -= d
            d = -d
    while (func(x0) > func(x0 + d)):
        x0 += d
        d *= 2
    return [x0, x0 + d]

c = linear_search(0, 0.000001)
print(c)