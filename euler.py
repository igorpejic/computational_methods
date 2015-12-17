# 17-12-2015
# free fall problem

# du/dz -----> it is function u=f(z)
# here it is v=f(t)

import numpy as np
import matplotlib.pyplot as plt

import scipy.integrate as integrate

m = 90
g = 9.81
# drag coefficient of closed parachute
c_d_c = 1

# drag coefficent of open parachute
c_d_o = 1.75

t_0 = 0
v_0 = -0.1

# final time, terminal speed reached
t_f = 30

# number of discretization intervals
n = 100


def f(v, t):
    if t < 15:
        c_d = c_d_c
    else:
        c_d = c_d_o
    return (m * g - c_d * v**2)/m

t = np.linspace(t_0, t_f, n + 1)
v = np.zeros_like(t)

v[0] = v_0

dt = t[1] - t[0]

for i in range(0, n):
    v[i+1] = v[i] + dt * f(v[i], t[i])

plt.plot(t, v, 'b--', label='euler')

# ode - ordered differntial equation , int - integration
# v_0 - y , t - x  (in dy/dx = y') n.b.
v1 = integrate.odeint(f, v_0, t)
plt.plot(t, v, 'r-', label='odeint')

plt.legend()
plt.xlabel('time [s]')
plt.ylabel('velocity [m/s]')
plt.grid()

plt.savefig('example.jpg')
plt.show()
