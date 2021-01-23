import numpy as np


class Matrix:
    def __init__(self, u_matrix):
        self.__matrix = np.array(u_matrix)

    def __eq__(self, other):
        return self.__matrix.shape == other.__matrix.shape

    def __add__(self, other):
        return Matrix(self.__matrix + other.__matrix)

    def __str__(self):
        return f'{self.__matrix}'


try:
    matrix_0 = Matrix([[1, 2, 3], [1, 4, 5]])
    matrix_1 = Matrix([[1, 2, 3], [1, 4, 5]])
    if matrix_0 == matrix_1:
        print(f'Матрица_1:\n{matrix_0}\n')
        print(f'Матрица_2:\n{matrix_1}\n')
        print(f'Сумма матриц:\n{matrix_0+matrix_1}')
    else:
        print(f'Ошибка: для сложения матрицы должны быть одного размера')
except TypeError:
    print('Ошибка: неверный тип входных данных')
