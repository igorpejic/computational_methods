import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

A = np.loadtxt("A.dat")
B = np.loadtxt("B.dat")

B = B * B

Y = np.linalg.solve(A, B)
print Y

plt.plot(Y, 'rs')

x = np.linspace(0, len(Y)-1, len(Y))

f = interpolate.interp1d(x, Y, kind=3)

x = np.linspace(0, len(Y)-1, 200)
print x

y = f(x)
print y

plt.plot(x, y, 'go')

plt.grid()

plt.show()
