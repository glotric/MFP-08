import numpy as np
import matplotlib.pyplot as plt
import scipy as sc

import tridiagonal as tridig
import bvp
import diffeq as deq


def npj(y, t, delta=1):
    return np.array([y[1], -delta * np.exp(y[0])])

t = np.linspace(0, 1, 50)
tol = 0.001

eigfunc = bvp.shoot(npj, 0, 0, 2, 1, t, tol)
print(eigfunc)

for i in range(len(eigfunc)):
    print(i)
    plt.plot(t, eigfunc[i], label=f'iteracija: {i}')

plt.legend()
plt.show()