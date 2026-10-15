"""Diagonal system: x_i = b_i/a_ii."""
from common import copy_system

def solve(A,b):
    A,b=copy_system(A,b)
    for i,row in enumerate(A):
        for j,v in enumerate(row):
            if i != j and abs(v)>1e-12: raise ValueError('A is not diagonal')
        if abs(row[i])<=1e-12: raise ValueError('Zero diagonal')
    return [b[i]/A[i][i] for i in range(len(A))]
