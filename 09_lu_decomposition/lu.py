"""Doolittle LU without pivoting: A=LU, then Ly=b and Ux=y."""
from common import copy_system, backward, forward

def factorize(A):
    """Return L and U; requires nonzero pivots without row swaps."""
    n=len(A)
    if n==0 or any(len(row)!=n for row in A): raise ValueError('Square matrix required')
    U=[[float(v) for v in row] for row in A]
    L=[[1.0 if i==j else 0.0 for j in range(n)] for i in range(n)]
    for k in range(n-1):
        if abs(U[k][k])<=1e-12: raise ValueError('Zero pivot; use pivoted LU')
        for i in range(k+1,n):
            m=U[i][k]/U[k][k]
            L[i][k]=m  # Store exactly the Gauss multiplier in L.
            for j in range(k+1,n): U[i][j]-=m*U[k][j]
            U[i][k]=0.0
    if abs(U[-1][-1])<=1e-12: raise ValueError('Singular matrix')
    return L,U

def solve(A,b):
    A,b=copy_system(A,b)
    L,U=factorize(A)
    y=forward(L,b)  # Step 1: lower triangular solve.
    return backward(U,y)  # Step 2: upper triangular solve.
