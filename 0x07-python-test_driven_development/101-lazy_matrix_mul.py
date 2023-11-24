#!/usr/bin/python3
"""
multiply 2 matricies using numpy module
"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """
    Multiply two matrices using the numpy module.

    Args:
        m_a (list of lists): The first matrix.
        m_b (list of lists): The second matrix.

    Returns:
        numpy.ndarray: The product matrix.
    """
    return numpy.matmul(m_a, m_b)
