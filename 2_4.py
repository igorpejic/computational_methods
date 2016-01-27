import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize


TH = np.loadtxt('lol.txt')

T = TH[: ,0]
H = TH[: ,1]

plt.plot(T, H, 'x')

k = np.polyfit(T, H, 2)


f_reg = np.poly1d(k)

x0 = optimize.fsolve(f_reg, [10, 45])

print x0

x = np.linspace(-10, 45, 200)
y = f_reg(x)

plt.plot(x, y)

plt.plot(x0[0], 0, 'r*', ms=20)

plt.show()
