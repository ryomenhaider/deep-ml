import numpy as np

def quotient_rule_derivative(g_coeffs: list, h_coeffs: list, x: float) -> float:


    # Your code here
    poly_g = np.poly1d(g_coeffs)
    poly_h = np.poly1d(h_coeffs)

    g_der = np.polyder(poly_g)
    h_der = np.polyder(poly_h)

    g_value = poly_g(x)
    h_value = poly_h(x)

    g_prime_val = g_der(x)
    h_prime_val = h_der(x)

    num = (g_prime_val * h_value) - (h_prime_val * g_value)
    denum = h_value **2
    return num / denum
    