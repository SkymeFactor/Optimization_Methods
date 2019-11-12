import math

phi = (1.0 + math.sqrt(5)) / 2


def func(x):
    return math.sin(x)

def golden_sec(eps, a, b, count, n):
    print("Iter: {}".format(count))
    print("a: {:.4f}, b: {:.4f}, length: {:.4f}".format(a, b, b - a))
    if abs(b - a) < eps:
        count = 1
        return (a + b) / 2
    else:
        t = (b - a) / phi
        x1, x2 = b - t , a + t
        if n == 'l':
            print("x1: ", x1, ", y1: ", func(x1))
        if n == 'r':
            print("x2: ", x2, ", y2: ", func(x2))
        if n == 'b':
            print("x1: ", x1, ", y1: ", func(x1))
            print("x2: ", x2, ", y2: ", func(x2))
        count += 1
        if func(x1) > func(x2):
            return golden_sec(eps, x1, b, count, 'r')
        else:
            return golden_sec(eps, a, x2, count, 'l')

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

x = golden_sec(0.000001, -(math.pi / 2), math.pi / 2, 1, 'b')
print("result x: ", x, ", result y: ", func(x))
c = linear_search(0, 0.000001)
print(c)
#print(golden_sec(0.000001, c[0], c[1]))