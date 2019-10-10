"""
Выполнить поворот(транспонирование) матрицы
"""

import numpy as np

matrix = np.array([[1, 0, 8], [3, 4, 1], [0, 4, 2]])
matrix = matrix.transpose()
print(matrix)
