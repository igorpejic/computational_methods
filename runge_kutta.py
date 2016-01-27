import numpy as np
import matplotlib.pyplot as plt

#  # NB exam: READ FROM FILE ############################################
############################################################
###################################################
###############################################

def f(x, y):
    return (np.sin(x) - 2*y) / x

x0 = 1
y0 = 1

# final x
xf = 10

# n of subdivisions
n = 5

err = 100.0

eps = 1e-9


# final y, referentni y
yr = 100.0


while err > eps:

    # begin computation ############
    n = n * 2

    dx = 1.0 * (xf - x0)/n

    X = np.linspace(x0, xf, n+1)
    Y = np.zeros_like(X)

    Y[0] = y0

    for i in range(n):
        k1 = f(X[i], Y[i])
        k2 = f(X[i] + 0.5*dx, Y[i] + dx*k1*0.5)
        k3 = f(X[i] + 0.5*dx, Y[i] + dx*k2*0.5)
        k4 = f(X[i] + dx, Y[i] + dx*k3)
        Y[i+1] = Y[i] + dx*(k1 + 2*k2 + 2*k3 + k4)/6

    err = np.abs(Y[-1] - yr)
    yr = Y[-1]
    print n, err

# end computation ###############


    plt.plot(X, Y, label='n:' + str(n))

import scipy.integrate as intgr


def fyx(y, x):
    return (np.sin(x) - 2*y) / x

# N.B. odeint accepts f(y, x) !!! --> that's why we have to defie fyx
Y_odeint = intgr.integrate.odeint(fyx, y0, X)
plt.plot(X, Y_odeint, label="ODEINT")

plt.legend()
plt.grid()
plt.xlabel('x')
plt.xlabel('y(x)')

plt.savefig('test.png')
