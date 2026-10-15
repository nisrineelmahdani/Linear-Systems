# Linear-Systems
# Solving Linear Systems — Mathematics for AI

## Project Overview

This repository contains Python implementations of fundamental numerical methods for solving systems of linear equations, developed as part of the **Mathematics for Artificial Intelligence** course.

The project explores different approaches to solving linear systems of the form **AX = B**, from direct analytical methods to numerical algorithms.

Each method is organized into a dedicated folder containing:
- Python implementation with explanatory comments.
- Mathematical principles and algorithm explanations.
- Numerical examples to demonstrate the method.
- Test cases to verify the correctness of the solutions.

### Methods Covered

1. **Cramer's Rule** — Solving linear systems using determinants.
2. **Diagonal Systems** — Direct solution of diagonal linear systems.
3. **Upper Triangular Systems** — Back substitution.
4. **Lower Triangular Systems** — Forward substitution.
5. **Gaussian Elimination Without Permutation** — Basic elimination algorithm.
6. **Gaussian Elimination With Row Permutation** — Handling zero pivots through row exchanges.
7. **Gaussian Elimination With Partial Pivoting** — Selecting the largest absolute pivot in the current column.
8. **Gaussian Elimination With Total Pivoting** — Selecting the largest absolute pivot in the remaining submatrix using row and column permutations.
9. **LU Decomposition** — Matrix factorization into lower and upper triangular matrices.

### Objectives

The main objective is to understand the mathematical foundations, implement the algorithms from scratch in Python, and compare their behavior, numerical stability, and computational efficiency.

This repository serves as both a practical implementation and an educational reference for numerical linear algebra in Artificial Intelligence and Data Science.
