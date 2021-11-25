#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    comp_matrix = []
    for i in matrix:
        comp_matrix.append(list(map(lambda x: x ** 2, i)))
    return comp_matrix
