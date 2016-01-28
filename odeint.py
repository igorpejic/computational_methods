# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 11:51:30 2016

@author: student
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate as intrp
import scipy.optimize as opt
import scipy.integrate as intgr

D1 = np.loadtxt('data1.txt')
D2 = np.loadtxt('data2.txt')

X1 = D1[:,0]
Y1 = D1[:,1]
X2 = D2[:,0]
Y2 = D2[:,1]

plt.plot(X1, Y1, 'rs', label='data 1')
plt.plot(X2, Y2, 'go', label='data 2')

f1 = intrp.interp1d(X1, Y1, kind='quadratic')

# limiti iz data 1 jer interpolacija ne radi van limita podataka
print X1
x1 = np.linspace(np.min(X1), np.max(X1), 300)
y1 = f1(x1)

plt.plot(x1, y1, 'r-', label='interpolacija')

k = np.polyfit(X2, Y2, 2) # dobijemo koeficijente polinoma
f2 = np.poly1d(k) # dobivamo funkciju f2(x)
y2 = f2(x1)

plt.plot(x1, y2, 'b--', label='regresija')

#Sjecišta funkcija f1 i f2


def razlika(x):
    return f1(x) - f2(x)

xs = opt.fsolve(razlika, [2, 10])
ys = f1(xs)

plt.plot(xs, ys, 'ko', ms=8, label='sjeciste')

I1 = intgr.quad(f1, xs[0], xs[1])[0]
I2 = intgr.quad(f2, xs[0], xs[1])[0]
I = I1 - I2
print I

# alternativno
print intgr.quad(razlika, xs[0], xs[1])[0]

xp = np.linspace(xs[0], xs[1], 200)
yp1 = f1(xp)
yp2 = f2(xp)

plt.fill_between(xp, yp1, yp2, color='orange')

plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.title('2. Python provjera')
plt.show()
