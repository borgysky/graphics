import matplotlib.pyplot as plt
import numpy as np

x = np.random.random_sample((3,))
y = np.random.random_sample((3,))
cells = 1000
nCPTS = np.size(x, 0)
n = nCPTS - 1
i = 0
t = np.linspace(0, 1, cells)
b = []
xbezier = np.zeros((1,cells))
ybezier = np.zeros((1,cells))

def Ni(n, i):
    return np.math.factorial(n) / (np.math.factorial(i) * np.math.factorial(n - i))

def basis(n, i, t):
    J = np.array(Ni(n, i) * (t**i) * (1 - t) ** (n - i))
    return J

for k in range(0, nCPTS):
    b.append(basis(n, i, t))
    xbezier = basis(n, i, t) * x[k] + xbezier
    ybezier = basis(n, i, t) * y[k] + ybezier
    i += 1

for line in b:
    plt.plot(t, line)
plt.show()