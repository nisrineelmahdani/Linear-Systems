"""Shared helpers: validation, substitution, and residual verification."""

def copy_system(A, b):
    """Return float copies of a nonempty square system without mutating inputs."""
    n = len(A)
    if n == 0 or len(b) != n or any(len(row) != n for row in A):
        raise ValueError("A must be nonempty and square; b must have length n")
    return [[float(value) for value in row] for row in A], [float(v) for v in b]


def backward(U, b, eps=1e-12):
    """Solve upper-triangular Ux=b, starting from the last row."""
    n = len(U)
    x = [0.0] * n
    for i in range(n-1, -1, -1):
        if abs(U[i][i]) <= eps:
            raise ValueError("Zero/near-zero diagonal: no unique solution from this factorization")
        s = sum(U[i][j] * x[j] for j in range(i+1, n))
        x[i] = (b[i] - s) / U[i][i]
    return x


def forward(L, b, eps=1e-12):
    """Solve lower-triangular Ly=b, starting from the first row."""
    n = len(L)
    y = [0.0] * n
    for i in range(n):
        if abs(L[i][i]) <= eps:
            raise ValueError("Zero/near-zero diagonal: cannot use forward substitution")
        s = sum(L[i][j] * y[j] for j in range(i))
        y[i] = (b[i] - s) / L[i][i]
    return y


def residual(A, x, b):
    """Maximum absolute entry of Ax-b (should be close to zero)."""
    return max(abs(sum(a*xj for a, xj in zip(row, x)) - bi) for row,bi in zip(A,b))
