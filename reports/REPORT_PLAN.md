# Assignment — report plan

## Report 1: Gauss with partial pivoting
1. Introduction and problem `Ax=b`
2. Motivation: zero/small pivots
3. Pivot rule: `p = argmax_{i>=k} |a_ik|`
4. Row swapping and elimination equations
5. Worked 3×3 example with every intermediate augmented matrix
6. Pseudocode and reference to `07_gauss_partial_pivoting/`
7. Numerical verification `Ax-b`, strengths and limitations

## Report 2: Gauss with total pivoting
1. Introduction; contrast with partial pivoting
2. Pivot rule: `(p,q) = argmax_{i,j>=k} |a_ij|`
3. Row and column exchanges, tracking the variable permutation
4. Worked 3×3 example requiring both types of swaps
5. Pseudocode and reference to `08_gauss_total_pivoting/`
6. Numerical verification `Ax-b`, computational costs and conclusion

## Python submission
- `06_gauss_row_permutation/`: exchanges a row if the current pivot is zero.
- `08_gauss_total_pivoting/`: exchanges rows and columns, restores original variable order.
- Run `python3 -m unittest discover -s tests -v` and include test results/screenshots if requested.
