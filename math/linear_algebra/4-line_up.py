#!/usr/bin/env python3
"""
adds array
"""


def add_arrays(arr1, arr2):
    """
    method to adds two arrays element-wise
    """
    if len(arr1) != len(arr2):
        return None

    new_array = []
    for i in range(len(arr1)):
        new_array.append(arr1[i] + arr2[i])

    return new_array
