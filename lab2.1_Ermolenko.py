# Лабораторная работа № 2.1
# Ермоленко В.Р., ІО-71
# №  n w    N
# 5  14 2000 256

# Додаткове завдання: реалізувати "табличний" метод

import random as r
import math
import matplotlib.pyplot as plt
import numpy as np
import datetime

n = 10
w_max = 1200
N = 64


def dft_matrix(N):
    i, j = np.meshgrid(np.arange(N), np.arange(N))
    return np.power(np.exp(- 2 * math.pi * 1J / N), i * j) / math.sqrt(N)


# Порівняння часу виконання звичайного методу та "табличного" для 4 <= N <= 640
def_times = []
table_times = []

for N_var in range(4, N*10+1, 16):
    default = datetime.datetime.now()
    w_real = [[math.cos(2 * math.pi * i * j / N_var) for j in range(N_var)] for i in range(N_var)]
    w_imag = [[math.sin(2 * math.pi * i * j / N_var) for j in range(N_var)] for i in range(N_var)]
    default = datetime.datetime.now() - default
    def_times.append(default.total_seconds() * (10 ** 6) + default.microseconds)

    table = datetime.datetime.now()
    dft_matrix(N_var)
    table = datetime.datetime.now() - table
    table_times.append(table.total_seconds() * (10 ** 6) + table.microseconds)

plt.plot([n for n in range(4, N*10+1, 16)], def_times)
plt.show()
plt.plot([n for n in range(4, N*10+1, 16)], table_times)
plt.show()
exit(0)


x = [0] * N


for i in range(n):
    A = r.randrange(2)
    W = r.randrange(w_max)
    f = r.randrange(1000000)
