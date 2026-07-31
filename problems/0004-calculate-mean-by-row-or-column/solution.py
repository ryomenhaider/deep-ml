def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	def mean(data): return sum(data)/len(data)
	
	if mode == 'column':
		return [mean(list(row)) for row in zip(*matrix)]
	if mode == 'row':
		return [mean(row) for row in matrix]