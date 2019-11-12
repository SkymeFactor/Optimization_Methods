import math

def func(x):
    return math.sin(x)

a1, b1 = -math.pi/2, math.pi/2

e = 0.001

def half_divide_method(a, b):
    x = (a + b) / 2
    count = 0
    while math.fabs(b - a) >= e:
        x = (a + b) / 2
        if func(x - e) > func(x + e):
            a = x
        else:
            b = x
        count = count+1
    return (a + b)/2


print ("x : ", half_divide_method(a1, b1))