"""Cramer's rule: x_j = det(A_j)/det(A). Best for learning/small matrices."""
from common import copy_system

def determinant(A):
    """Compute a determinant by cofactor expansion (slow: teaching only)."""
    n = len(A)
    if n == 1: return A[0][0]
    if n == 2: return A[0][0]*A[1][1]-A[0][1]*A[1][0]
    return sum((-1)**j * A[0][j] * determinant([row[:j]+row[j+1:] for row in A[1:]]) for j in range(n))

def solve(A, b):
    A,b = copy_system(A,b)
    d = determinant(A)
    if abs(d) <= 1e-12: raise ValueError('det(A)=0 (or numerically tiny)')
    # Replace each coefficient column with b, one at a time.
    return [determinant([[b[i] if k == j else A[i][k] for k in range(len(A))] for i in range(len(A))])/d for j in range(len(A))]
