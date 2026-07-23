import numpy as np

def product_rule_derivative(f_coeffs: list, g_coeffs: list) -> list:
    p_f = np.polynomial.polynomial.Polynomial(f_coeffs)
    p_g = np.polynomial.polynomial.Polynomial(g_coeffs)
    
    p_f_deriv = p_f.deriv()
    p_g_deriv = p_g.deriv()
    
    result_poly = (p_f_deriv * p_g) + (p_f * p_g_deriv)
    
    coef = np.round(result_poly.coef, 4).tolist()
    
    while len(coef) > 1 and coef[-1] == 0.0:
        coef.pop()
        
    return coef
    
