#!/usr/bin/python3
def matrix_mul(m_a, m_b):
    # Validate m_a and m_b
    for matrix, name in [(m_a, 'm_a'), (m_b, 'm_b')]:
        if not isinstance(matrix, list):
            raise TypeError(f"{name} must be a list")
        if not all(isinstance(row, list) for row in matrix):
            raise TypeError(f"{name} must be a list of lists")
        if not matrix or any(not row for row in matrix):
            raise ValueError(f"{name} can't be empty")
        if any(not isinstance(element, (int, float)) for row in matrix for element in row):
            raise TypeError(f"{name} should contain only integers or floats")
        if len(set(len(row) for row in matrix)) > 1:
            raise TypeError(f"Each row of {name} must be of the same size")

    # Validate if m_a and m_b can be multiplied
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Multiply matrices
    result = [[sum(a * b for a, b in zip(row_a, col_b)) for col_b in zip(*m_b)] for row_a in m_a]

    return result

