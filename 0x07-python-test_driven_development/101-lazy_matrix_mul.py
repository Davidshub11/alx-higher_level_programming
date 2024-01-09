#!/usr/bin/python3
import numpy as np

def lazy_matrix_mul(m_a, m_b):
    try:
        result = np.matmul(m_a, m_b)
        return result.tolist()
    except ValueError as ve:
        raise ValueError(f"m_a and m_b can't be multiplied") from ve
    except Exception as e:
        raise e

