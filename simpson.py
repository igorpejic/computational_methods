import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as intgr

# fun
plt.xcd()


def f(x):
    return -25 * x + 200 * x**2 + 400 * x**4 - 500 * x**5


a = input("a:")
b = input("b:")

# n - broj podintervala
n = 1

while n % 2 != 0:
    n = input("n:")

x = np.linspace(a, b, 200)
y = f(x)

# if we want to fill between two functions -- (x, y1, y2)
plt.fill_between(x, y, color='orange', alpha=0.2)
plt.plot(x, y, color='blue', lw=2)  # color-shorter ->  c
plt.show()
plt.savefig('example.jpg')

# intervali integracije
X = np.linspace(a, b, n+1)
Y = f(X)

dx = X[1] - X[0]

# draw only points
plt.plot(X, Y, "ro")
plt.show()
plt.savefig('example.jpg')

# integral
I = 0

for i in range(0, n, 2):
    p = 1./3 * dx * (Y[i] + 4 * Y[i+1] + Y[i+2])
    I += p
    print i, p

print "simpson 1/3:", I
# trapz formula
print "trapz:", np.trapz(Y, X)
print "quad: ", intgr.quad(f, a, b)[0]
