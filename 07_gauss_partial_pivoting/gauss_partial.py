"""Gauss with partial pivoting: largest |A[i][k]| in current column."""
from common import copy_system, backward

def solve(A,b):
    A,b=copy_system(A,b)
    n=len(A)
    for k in range(n-1):
        p=max(range(k,n),key=lambda i:abs(A[i][k]))
        if abs(A[p][k])<=1e-12: raise ValueError('Singular matrix')
        # Exchange whole equations, including b.
        A[k],A[p]=A[p],A[k]
        b[k],b[p]=b[p],b[k]
        for i in range(k+1,n):
            m=A[i][k]/A[k][k]
            for j in range(k+1,n): A[i][j]-=m*A[k][j]
            b[i]-=m*b[k]
            A[i][k]=0.0
    return backward(A,b)
