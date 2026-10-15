"""Gaussian elimination without any row exchanges."""
from common import copy_system, backward

def solve(A,b):
    A,b=copy_system(A,b)
    n=len(A)
    for k in range(n-1):
        if abs(A[k][k])<=1e-12: raise ValueError('Zero pivot: use a pivoting method')
        for i in range(k+1,n):
            m=A[i][k]/A[k][k]  # elimination multiplier m_ik
            for j in range(k+1,n):
                A[i][j]-=m*A[k][j]
            b[i]-=m*b[k]       # apply operation to right-hand side too
            A[i][k]=0.0
    return backward(A,b)
