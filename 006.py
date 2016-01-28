import numpy as np
import matplotlib.pyplot as plt

from scipy import optimize


def f(x):
    return 0.1 * x**3 - x**2 - 5*x + 10


def g(x):
    return 0.3 * x**2 - 2*x - 5

X = np.linspace(-10, 15, 5000)
Y = f(X)
Y1 = g(X)


x0, x1 = optimize.fsolve(g, [-100, 150])
x0, x1 = min([x0, x1]), max([x0, x1])
print x0, x1
y0 = g(x0)
print y0

plt.plot(x0, f(x0), 'go')
plt.plot(x1, f(x1), 'ro')

k = np.polyfit([x0, x1], [f(x0), f(x1)], 1)

xr = np.linspace(-10, 15, 5000)

y = xr * k[0] + k[1]

# plt.plot(xr, y)

f = np.poly1d(k)

y2 = f(xr)

plt.plot(xr, y2, 'r')

plt.grid()
plt.plot(X, Y)
plt.plot(X, Y1)
plt.show()
