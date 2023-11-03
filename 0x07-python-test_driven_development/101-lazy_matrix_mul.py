#!/usr/bin/python3
"""Module to multiply matrices
"""

import numpy as np
"""Import from the module"""

def validate_matrix(matrix, name):
    """This function Check if matrix is a list"""
    if not isinstance(matrix, list):
        raise TypeError(f"{name} must be a list")
    
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError(f"{name} must be a list of lists")

    if not matrix:
        raise ValueError(f"{name} can't be empty")

    for row in matrix:
        if not all(isinstance(x, (int, float)) for x in row):
            raise TypeError(f"{name} should contain only integers or floats")

    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError(f"Each row of {name} must be of the same size")

def lazy_matrix_mul(m_a, m_b):
    """This function multiply two matrices using Numpy"""
    try:
        validate_matrix(m_a, "m_a")
        validate_matrix(m_b, "m_b")

        matrix_a = np.array(m_a)
        matrix_b = np.array(m_b)

        if matrix_a.shape[1] != matrix_b.shape[0]:
            raise ValueError("m_a and m_b can't be multiplied")

        result = np.dot(matrix_a, matrix_b)
        return result.tolist()
    except ValueError as e:
        raise ValueError(str(e))
    except (TypeError, AttributeError) as ee:
        raise TypeError(str(ee))
