# dla beta 3 musi wyjść 0, 1, 1, 0

from numpy import exp

beta = 3


def f(x):
    answer = 1 / (1 + exp(-beta * x))
    return answer


u = [[0, 0, 1], [1, 0, 1], [0, 1, 1], [1, 1, 1]]
w = [[2, 2, -3], [2, 2, -1]]
s = [-2, 2, -1]
x_array = []


def calculate_x1(w, u):
    array = []
    for p in range(4):
        x = 0
        for j in range(3):
            x += w[0][j] * u[p][j]
        array.append(f(x))
    return array


def calculate_x2(w, u):
    array = []
    for p in range(4):
        x = 0
        for j in range(3):
            x += w[1][j] * u[p][j]
        array.append(f(x))
    return array


x1 = calculate_x1(w, u)
x_array.append(x1)
x2 = calculate_x2(w, u)
x_array.append(x2)
x_array.append([1, 1, 1, 1])
print(x_array)


def y():
    answer = []
    for p in range(4):
        tmp = 0
        for i in range(3):
            tmp += s[i] * x_array[i][p]
        answer.append(f(tmp))
    return answer


dgnk = y()
print(dgnk)


