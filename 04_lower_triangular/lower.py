"""Lower triangular system solved by forward substitution."""
from common import copy_system, forward

def solve(A,b):
    A,b=copy_system(A,b)
    if any(abs(A[i][j])>1e-12 for i in range(len(A)) for j in range(i+1,len(A))):
        raise ValueError('A is not lower triangular')
    return forward(A,b)
