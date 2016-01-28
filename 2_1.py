import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as sci


def f(y, x):
    return np.cos(x)/(y*y + x*x)

x = np.linspace(0, 10, 25)

x0 = 0
y0 = 1

y_odeint = sci.odeint(f, y0, x)

plt.plot(y_odeint, label="odeint")
plt.plot(x0,  y0, 'r*', ms=100)
plt.xlabel('x')
plt.ylabel('y(x)')
plt.legend()
plt.grid()
# plt.show()

import scipy.interpolate as interpolate
y_odeint = [y[0] for y in y_odeint]

f_interpolation = interpolate.interp1d(x, y_odeint, kind='linear')

x_new = [1.11 + 1.11 * i for i in range(9)]
y_new = f_interpolation(x_new)

plt.plot(y_new, 'bo', label="interpolation")
plt.show()
