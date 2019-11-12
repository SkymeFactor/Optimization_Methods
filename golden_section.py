import math

phi = (1.0 + math.sqrt(5)) / 2


def func(x):
    return math.sin(x)

def golden_sec(eps, a, b):
    if abs(b - a) < eps:
        return (a + b) / 2
    else:
        t = (b - a) / phi
        x1, x2 = b - t , a + t
        if func(x1) > func(x2):
            return golden_sec(eps, x1, b)
        else:
            return golden_sec(eps, a, x2)


x = golden_sec(0.000001, -(math.pi / 2), math.pi / 2)
print("result x: ", x, ", result y: ", func(x))