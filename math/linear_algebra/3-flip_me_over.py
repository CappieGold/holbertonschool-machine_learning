#!/usr/bin/env python3
"""
Transpose a 2D matrix
"""


def matrix_transpose(matrix):
    """
    methode to transpose matrix
    """
    rows = len(matrix)
    cols = len(matrix[0])

    transposed = []
    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(matrix[i][j])
        transposed.append(new_row)

    return transposed
