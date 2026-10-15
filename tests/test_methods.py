"""Unit tests requiring only the standard Python library."""
import unittest
from run import EXAMPLES, load_solver
from common import residual

class TestMethods(unittest.TestCase):
    def test_every_demonstration(self):
        for name,(A,b) in EXAMPLES.items():
            with self.subTest(method=name):
                x=load_solver(name)(A,b)
                self.assertLess(residual(A,x,b),1e-9)

    def test_gauss_variants_same_solution(self):
        A=[[2,1,-1],[3,2,2],[4,-2,3]]
        b=[1,13,9]
        for name in ['05_gauss_without_permutation','06_gauss_row_permutation',
                     '07_gauss_partial_pivoting','08_gauss_total_pivoting']:
            with self.subTest(method=name):
                result=load_solver(name)(A,b)
                for v,expected in zip(result,[1,2,3]):
                    self.assertAlmostEqual(v,expected)

    def test_column_permutation_is_undone(self):
        A=[[0,2,1],[1,0,3],[2,1,8]]
        self.assertEqual([round(v,8) for v in load_solver('08_gauss_total_pivoting')(A,[7,10,28])],[1,2,3])

    def test_zero_pivot_requires_permutation(self):
        A=[[0,1],[2,3]]
        b=[2,8]
        with self.assertRaises(ValueError): load_solver('05_gauss_without_permutation')(A,b)
        self.assertLess(residual(A,load_solver('06_gauss_row_permutation')(A,b),b),1e-10)

if __name__=='__main__': unittest.main()
