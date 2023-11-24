#!/usr/bin/python3
"""matrix_mul method."""


def matrix_mul(m_a, m_b):
    """Multiply two matrices.

    This function multiplies two matrices, m_a and m_b, and returns the result.

    Args:
        m_a (list): The first matrix.
        m_b (list): The second matrix.

    Returns:
        list: The product matrix.

    Raises:
        TypeError: If m_a or m_b are not lists.
        TypeError: If m_a or m_b are not lists of lists.
        ValueError: If m_a or m_b are empty lists/matrices.
        TypeError: If m_a or m_b contain a non int/float.
        TypeError: If m_a or m_b are not rectangular.
        ValueError: If m_a or m_b can't be multiplied.
    """

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    m_a_e = False
    m_b_e = False
    m_a_n = False
    m_b_n = False
    m_a_notn = False
    m_b_notn = False
    for w in m_a:
        if not isinstance(w, list):
            raise TypeError("m_a must be a list of lists")
        if len(w) != len(m_a[0]):
            m_a_n = True
        for m in w:
            if not isinstance(m, (int, float)):
                m_a_notn = True

    for w in m_b:
        if not isinstance(w, list):
            raise TypeError("m_b must be a list of lists")
        if len(w) != len(m_b[0]):
            m_b_n = True
        for m in w:
            if not isinstance(m, (int, float)):
                m_b_notn = True

    if len(m_a) == 0 or (len(m_a) == 1 and len(m_a[0]) == 0):
        raise ValueError("m_a can't be empty")

    if len(m_b) == 0 or (len(m_b) == 1 and len(m_b[0]) == 0):
        raise ValueError("m_b can't be empty")

    if m_a_notn:
        raise TypeError("m_a should contain only integers or floats")

    if m_b_notn:
        raise TypeError("m_b should contain only integers or floats")

    if m_a_n:
        raise TypeError("each row of m_a must should be of the same size")

    if m_b_n:
        raise TypeError("each row of m_b must should be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    r = [[] for it in range(len(m_a))]

    for it in range(len(m_a)):
        for jt in range(len(m_b[0])):
            co = 0
            for d in range(len(m_b)):
                co += m_a[it][d] * m_b[d][jt]
            r[it].append(co)

    return r


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/100-matrix_mul.txt")
