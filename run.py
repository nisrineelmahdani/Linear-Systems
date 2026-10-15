"""Command-line demos; run `python run.py --list` to see methods."""
import importlib.util
import sys
from pathlib import Path
from common import residual

EXAMPLES = {
 '01_cramer': ([[2,1,-1],[3,2,2],[4,-2,3]],[1,13,9]),
 '02_diagonal': ([[2,0,0],[0,3,0],[0,0,5]],[8,9,20]),
 '03_upper_triangular': ([[2,1,-1],[0,3,2],[0,0,4]],[5,10,8]),
 '04_lower_triangular': ([[2,0,0],[1,3,0],[4,-2,5]],[4,8,12]),
 '05_gauss_without_permutation': ([[2,1,-1],[3,2,2],[4,-2,3]],[1,13,9]),
 '06_gauss_row_permutation': ([[0,2,1],[2,1,-1],[1,3,2]],[4,1,7]),
 '07_gauss_partial_pivoting': ([[2,1,-1],[3,2,2],[4,-2,3]],[1,13,9]),
 '08_gauss_total_pivoting': ([[0,2,1],[1,0,3],[2,1,8]],[7,10,28]),
 '09_lu_decomposition': ([[2,1,1],[4,3,3],[8,7,9]],[5,13,35]),
}

def load_solver(folder):
    code=next((Path(__file__).parent/folder).glob('*.py'))
    spec=importlib.util.spec_from_file_location('method_solver',code)
    module=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.solve

def main():
    if len(sys.argv)!=2 or sys.argv[1]=='--list':
        print('Usage: python run.py METHOD | all | --list')
        for name in EXAMPLES: print(' ',name)
        return
    names=list(EXAMPLES) if sys.argv[1]=='all' else [sys.argv[1]]
    for name in names:
        A,b=EXAMPLES[name]
        x=load_solver(name)(A,b)
        print(f'{name}: x={x}; max |Ax-b|={residual(A,x,b):.2e}')

if __name__=='__main__': main()
