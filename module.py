import math


def func(x):
    return math.atan(x) + x - 1


def bisection(func, a: int, b: int, eps):
    if func(a) * func(b) >= 0:
        print("There is no root in this interval")
        return None

    while (b - a) / 2 > eps:
        midpoint = (a + b) / 2
        if func(midpoint) == 0:
            return midpoint
        elif func(a) * func(midpoint) < 0:
            b = midpoint
        else:
            a = midpoint

    return (a + b) / 2

start = -100
end = 100
eps = 0.0001

root = bisection(func, start, end, eps)
if root is not None:
    print(f"Root of the arctg(x) + x - 1 = 0 on the interval from -100 to 100: {root:.4f}")
