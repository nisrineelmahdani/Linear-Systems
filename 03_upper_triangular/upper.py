"""Upper triangular system solved by back substitution."""
from common import copy_system, backward

def solve(A,b):
    A,b=copy_system(A,b)
    if any(abs(A[i][j])>1e-12 for i in range(len(A)) for j in range(i)):
        raise ValueError('A is not upper triangular')
    return backward(A,b)
