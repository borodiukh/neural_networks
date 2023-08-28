import random
import math

# sample
x_s = [0, 0, 0, 0, 0,
       0, 1, 1, 0, 0,
       0, 0, 1, 0, 0,
       0, 0, 1, 0, 0,
       0, 0, 1, 0, 0]

x = [0 for i in range(25)]

c = [[0 for i in range(25)] for i in range(25)]
theta = [0 for i in range(25)]
w = [[0 for i in range(25)] for i in range(25)]

u = [0 for i in range(25)]

T = 1.5  # 0.5 < T < 20
loops = 10


def make_c():
    for i in range(25):
        for j in range(25):
            c[i][j] = (x_s[i] - 0.5) * (x_s[j] - 0.5)
        c[i][i] = 0


def make_theta():
    for i in range(25):
        theta[i] = 0
        for j in range(25):
            theta[i] = theta[i] + c[i][j]


def make_w():
    w = c[:]
    w = 2 * w


def make_u(i, t):
    u[i] = 0
    for j in range(25):
        u[i] = u[i] + w[i][j] * x[j]
    u[i] = u[i] - theta[i]


def f(a):
    return 1 / (1 + math.exp(-a / T))


def make_x(i, t):
    if t == 0:
        x[i] = random.getrandbits(1)
    else:

        make_u(i, t - 1)
        if random.random() <= f(u[i]):
            x[i] = 1
        else:
            x[i] = 0


def print_x():
    for i in range(5):
        for j in range(5):
            if x[i * 5 + j] == 1:
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print("\n")
    print("----------")


# main loop
make_c()
make_theta()
make_w()

# time
for t in range(loops):
    for i in range(25):
        make_x(i, t)
    print_x()

