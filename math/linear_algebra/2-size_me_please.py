#!/usr/bin/env python3
"""
calculates the shape of a matrix
"""


def matrix_shape(matrix):
    """Calculate the shape of a matrix recursively"""
    shape = []
    
    # Ajouter la taille de la dimension actuelle
    shape.append(len(matrix))
    
    # Si le premier élément est encore une liste/matrice, continuer récursivement
    if isinstance(matrix[0], list):
        # Obtenir la forme des dimensions suivantes
        remaining_shape = matrix_shape(matrix[0])
        # Combiner avec la dimension actuelle
        shape.extend(remaining_shape)
    
    return shape
