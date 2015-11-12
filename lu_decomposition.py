# 11-12-2015
# LU decomposition

import numpy as np

A = np.loadtxt('a.txt')
B = np.loadtxt('b.txt')
print A
print B

# det has to be != 0
print np.linalg.det(A)

# broj nepoznanica
n = np.size(B)
print n

L = np.zeros([n, n])
print L
L = np.zeros(np.shape(A))

U = np.zeros_like(A)


# LU decomposition
for k in range(n):
    for i in range(k, n):
        sum = 0
        for m in range(k):
            sum += L[i, m] * U[m, k]
        L[i, k] = A[i, k] - sum
    for j in range(k+1, n):
        sum = 0
        for m in range(k):
            sum += L[k, m] * U[m, j]
        U[k, j] = (A[k, j] - sum) / L[k, k]

# algorithm doesn't set ones on U
for i in range(n):
    U[i, i] = 1


# check algorithm
print np.dot(L, U)
print A

C = np.zeros_like(B)


for i in range(n):
    sum = 0
    for j in range(0, i):
        sum += L[i, j] * C[j]
    C[i] = (B[i] - sum) / L[i, i]

# check B
print np.dot(L, C)
print B


X = np.zeros_like(B)

# NB: negative step needed
for i in range(n-1, -1, -1):
    sum = 0
    for j in range(i+1, n):
        sum += U[i, j] * X[j]
    X[i] = C[i] - sum

print X

# check X
print np.dot(U, X)
print C


# check original equation (A * x = B)
print np.dot(A, X)
print B


# ---------------------------------------------------------------
# on exam:
# numpy based solution

X1 = np.linalg.solve(A, B)
print X1
print X
