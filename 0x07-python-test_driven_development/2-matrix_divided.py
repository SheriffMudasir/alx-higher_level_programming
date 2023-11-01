#!/usr/bin/python3
"""This file contains one function for dividing elements of a matrix"""
def matrix_divided(matrix, div):

        """
        This function divides all elements in a matrix.

        Args:
                a (matrix): List of lists of elements.
                b (int or float): div element to divide with.

        Returns:
                List: A new matrix(List of lists).
        """
        for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                        if not isinstance(matrix[i][j], (int, float)):
                                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
                        
        for i in range(len(matrix)):
                size = len(matrix[0])
                if len(matrix[i]) != size:
                        raise TypeError("Each row of the matrix must have the same size")
        if not isinstance(div, (int, float)):
                raise TypeError("div must be a number")
        if div == 0:
                raise ZeroDivisionError("division by zero")
        
        for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                        division = matrix[i][j] / div
                        matrix[i][j] = round(division, 2)
        return matrix



        
