import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt


def f(x):
    return np.sin(x) * np.cos(x) / 2

x = np.linspace(1, 4, 500)
y = f(x)
y1 = np.zeros_like(x)

plt.plot(x, y, 'y')
plt.plot(x, y1, 'b')

x0 = optimize.fsolve(f, 1)
x1 = optimize.fsolve(f, 3)

y2 = f(np.linspace(x0, x1, 500))


print np.trapz(np.linspace(x0, x1, 500), y)
plt.fill_between(np.linspace(x0, x1, len(x)), f(np.linspace(x0, x1, len(x))), np.zeros_like(y))

X = np.linspace(x0, x1, 20)

k = np.polyfit(X, f(X), 10)

f2 = np.poly1d(k)

y2 = f2(X)

plt.plot(X, y2)

I2 = np.trapz(X, y2)
print I2

plt.show()

