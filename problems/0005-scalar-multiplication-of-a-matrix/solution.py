def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	for idx, i in enumerate(matrix):
		for idx1, j in enumerate(i):
			matrix[idx][idx1] = matrix[idx][idx1] * scalar
	return matrix