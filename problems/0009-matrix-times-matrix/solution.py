def matrixmul(A: list[list[int | float]], B: list[list[int | float]]) -> list[list[int | float]]:
    if len(B) != len(A[0]):
        return -1
    B_cols = list(zip(*B))
    return [[sum(a * b for a, b in zip(row_a, col_b)) for col_b in B_cols] for row_a in A]
