import numpy as np

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]] | str:
    try:
        A_arr = np.array(A, dtype=float)
        T_arr = np.array(T, dtype=float)
        S_arr = np.array(S, dtype=float)
        
        if np.isclose(np.linalg.det(T_arr), 0.0) or np.isclose(np.linalg.det(S_arr), 0.0):
            return "-1"
            
        T_inv = np.linalg.inv(T_arr)
        
        return T_inv @ A @ S
        
    except (np.linalg.LinAlgError, ValueError, TypeError):
        return "-1"
