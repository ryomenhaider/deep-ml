import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
	# Your code here, make sure to round
    X = np.array(X)
    y = np.array(y)
    
    # Calculate theta using the closed-form normal equation: (X^T * X)^(-1) * X^T * y
    theta = np.linalg.inv(X.T @ X) @ X.T @ y
    
    # Round the results to 4 decimal places and convert back to a list
    return np.round(theta, decimals=4).tolist()