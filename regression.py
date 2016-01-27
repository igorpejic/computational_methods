from numpy import*
from matplotlib.pyplot import*

XY = loadtxt('lol.txt')

M = shape(XY)
n = M[0]

X = XY[:,0]
Y = XY[:,1]

SX = sum(X)
SY = sum(Y)
SXY=sum(X*Y)
SX2 = sum(X**2)

A = array([[n,SX],
           [SX,SX2]])

B = array([SY,SXY])

a = linalg.solve(A,B)
print a

print polyfit(X,Y,1)

def F(x):
    return a[0] + a[1]*x
    
Xplot = array([min(X),max(X)])
plot(X,Y,'o')
plot(Xplot,F(Xplot), 'y')
title('regresijski pravac')
xlabel('x-koordinate')
ylabel('y-label')
grid()
show()
