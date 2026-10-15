"""Gauss with total pivoting: search remaining submatrix, swap rows AND columns."""
from common import copy_system, backward

def solve(A,b):
    A,b=copy_system(A,b)
    n=len(A)
    permutation=list(range(n))  # Current column j represents original variable permutation[j].
    for k in range(n-1):
        p,q=max(((i,j) for i in range(k,n) for j in range(k,n)),
                key=lambda ij:abs(A[ij[0]][ij[1]]))
        if abs(A[p][q])<=1e-12: raise ValueError('Singular matrix')
        # Row swap acts on the full augmented equation.
        A[k],A[p]=A[p],A[k]
        b[k],b[p]=b[p],b[k]
        # Column swap changes variable positions, but NOT b.
        for i in range(n): A[i][k],A[i][q]=A[i][q],A[i][k]
        permutation[k],permutation[q]=permutation[q],permutation[k]
        for i in range(k+1,n):
            m=A[i][k]/A[k][k]
            for j in range(k+1,n): A[i][j]-=m*A[k][j]
            b[i]-=m*b[k]
            A[i][k]=0.0
    y=backward(A,b)  # Solutions in the CURRENT (permuted) variable order.
    x=[0.0]*n
    for i in range(n): x[permutation[i]]=y[i]  # Undo column permutations.
    return x
