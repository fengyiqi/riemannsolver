from .mesh import Mesh
import numpy as np


def symmetry(cell_values, velocity: bool):
    cell_values_list = list(cell_values)
    # print(cell_values_list)
    if velocity:
        return np.array([-cell_values_list[0]] + cell_values_list + [-cell_values_list[-1]])
    else:
        return np.array([cell_values_list[0]] + cell_values_list + [-cell_values_list[1]])
