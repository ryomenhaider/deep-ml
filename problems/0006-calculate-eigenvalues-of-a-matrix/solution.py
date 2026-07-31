def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	t = matrix[0][0] + matrix[1][1]
	det = (matrix[0][0] * matrix[1][1]) - (matrix[0][1]* matrix[1][0])
	delta = (t**2 - 4*det)**0.5
	return [(t + delta) / 2, (t - delta) / 2]