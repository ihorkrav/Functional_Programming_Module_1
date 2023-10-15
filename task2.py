import math

def tabulate_function(start, end, step):
    x_values = []
    y_values = []

    x = start
    while x <= end:
        y = math.cos(x) / x
        x_values.append(x)
        y_values.append(y)
        x += step

    return x_values, y_values

start = 0.5
end = 11
step = 0.3

x_values, y_values = tabulate_function(start, end, step)

for x, y in zip(x_values, y_values):
    print(f"x = {x:.2f}, y = {y:.4f}")
