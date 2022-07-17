from sympy import Poly, Symbol, solve_poly_inequality
from sympy import Symbol, Poly, solve_rational_inequalities
from sympy import Symbol, solve, solve_univariate_inequality, sin
from sympy import sympify

def isolve(ineq_obj):
    
    x = Symbol('x')
    expr = ineq_obj.lhs
    rel = ineq_obj.rel_op

    if expr.is_polynomial():
        p = Poly(expr, x)
        return solve_poly_inequality(p, rel)
    elif expr.is_rational_function():
        numer, denom = expr.as_numer_denom()
        p1 = Poly(numer)
        p2 = Poly(denom)
        return solve_rational_inequalities([[((p1, p2), rel)]])
    else:
        return solve_univariate_inequality(ineq_obj, x, relational=False)
        

if __name__ == '__main__':
    
    equation = input('Enter your inequality expression in terms of x: ')

    try:
        ineq_equation = sympify(equation)
    except SymifyError:
        print('Invalid input')
    else:
        print(isolve(ineq_equation))




'''

Invalid does not work properly. 

'''
    
