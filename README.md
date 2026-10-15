# Solving Linear Systems — Mathematics for AI

A teaching-oriented Python repository covering **Chapter 3: Solving Linear Systems**. Each method lives in a numbered folder with explanatory comments and its own short README.

## Course order

| Folder | Topic | Key idea |
|---|---|---|
| `01_cramer` | Cramer's rule | Ratios of determinants |
| `02_diagonal` | Diagonal systems | Divide each equation by its diagonal coefficient |
| `03_upper_triangular` | Upper triangular | Back substitution |
| `04_lower_triangular` | Lower triangular | Forward substitution |
| `05_gauss_without_permutation` | Gauss without swapping | Elimination using m_ik = a_ik/a_kk |
| `06_gauss_row_permutation` | Gauss with row permutation | Swap rows only for a zero pivot |
| `07_gauss_partial_pivoting` | Gauss with partial pivoting | Maximum absolute pivot in current column |
| `08_gauss_total_pivoting` | Gauss with total pivoting | Maximum in remaining submatrix; swap rows and columns |
| `09_lu_decomposition` | Doolittle LU | A=LU, then Ly=b and Ux=y |

## Quick start

Python 3.9+; **no external dependencies**.

```bash
python3 run.py --list
python3 run.py 08_gauss_total_pivoting
python3 run.py all
python3 -m unittest discover -s tests -v
```

To use a method with your own matrix, import the method file or edit its example in `run.py`. Functions accept a square coefficient matrix `A` (list of lists) and right-hand side `b` (list), and return `x` as a list. Inputs are copied before elimination.

## Math notes

### Gaussian elimination

For pivot index `k` and row `i > k`, calculate `m = A[i][k] / A[k][k]`. Update `A[i][j] -= m*A[k][j]`, `b[i] -= m*b[k]`, then set `A[i][k] = 0`. Finish by back substitution.

### Partial vs total pivoting

* **Partial:** locate the largest absolute coefficient in column `k` among rows `k..n-1`. Swap complete equations (rows and corresponding `b` entries).
* **Total:** locate the largest absolute coefficient in the remaining submatrix. Swap rows and columns. Column swaps change the ordering of unknowns, so a `permutation` array is maintained and reversed in the final answer.

### LU

Doolittle LU stores the elimination multipliers below the diagonal of `L`, with ones on its diagonal. `U` is the upper matrix from elimination. The basic implementation assumes no pivoting is needed; pivoted LU would normally use `PA=LU`.

## Limitations and academic notes

* These are **educational implementations**, not production numerical solvers.
* A fixed numerical tolerance is used for zero/near-zero pivot checks; numerical robustness depends on matrix scaling.
* The basic LU and no-permutation implementations require usable pivots in their given order.
* Cramer's determinant uses recursive cofactors: it is intentionally simple but becomes impractical for large matrices.
* For reliable production numerical computation, prefer NumPy/SciPy.

## Assignment structure

The professor's assignment asks for a **report on partial pivoting**, a **report on total pivoting**, and **Python implementation of Gauss with row permutation and total pivoting**. See `reports/REPORT_PLAN.md` for the report outline; write the final explanations in your own words based on tested examples.
