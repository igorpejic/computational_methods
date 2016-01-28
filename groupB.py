# -*- coding: utf-8 -*-
"""
Created on Mon Jan 19 19:10:55 2015

@author: teo
"""
#from numpy import *
#import scipy
import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate as inter
import scipy.integrate as intgr

"""
grupa A
1. Kreiraj funkciju koja izračunava f(x,y) = (cos x)/(y2 + x2). {1b}
"""
def f(x,y):
    return np.cos(x)/(y**2 + x**2)
    
"""
2. Rješi dif. jednadžbu y' = f(x,y) na 25 točaka na intervalu x = [0,10], uz početni uvjet (x0,y0) = (0,1). {4b}

"""

x0=0
y0=1
X=np.linspace(0,10,25)
Y=intgr.odeint(f,y0,X)
print X
print Y
"""
3. Nacrtaj rješenje diferencijalne jednadžbe. {2b}
"""
plt.plot(X,Y,'ro')
#plt.show()
"""
4. Na istom grafu nacrtaj početni uvjet (crvena zvjezdica) i uključi mrežu pomoćnih linija. {2b}
"""
plt.plot(x0,y0,'r*')
plt.grid()
#plt.show()
"""
5. Pomoću linearne interpolacije rješenja 2. koraka, u petlji izračunaj y za sljedeće x-eve: 1.11, 2.22, 3.33, ... 9.99. {5b}
"""

Fint=inter.interp1d(X,Y[:,0],kind='linear')
plt.plot(X,Fint(X))
plt.show()
for i in range(1,10):
    print Fint(1.11*i)
