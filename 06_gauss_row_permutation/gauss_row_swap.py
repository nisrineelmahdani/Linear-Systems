"""Gauss with simple row permutation: swap only when pivot is zero."""
from common import copy_system, backward

def solve(A,b):
    A,b=copy_system(A,b)
    n=len(A)
    for k in range(n-1):
        if abs(A[k][k])<=1e-12:
            # Find the first usable row, not necessarily the largest pivot.
            p=next((i for i in range(k+1,n) if abs(A[i][k])>1e-12),None)
            if p is None: raise ValueError('No usable pivot in this column')
            A[k],A[p]=A[p],A[k]
            b[k],b[p]=b[p],b[k]
        for i in range(k+1,n):
            m=A[i][k]/A[k][k]
            for j in range(k+1,n): A[i][j]-=m*A[k][j]
            b[i]-=m*b[k]
            A[i][k]=0.0
    return backward(A,b)
