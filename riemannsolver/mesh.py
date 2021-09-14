import numpy as np


class Mesh:
    def __init__(self, x_start, x_end, n_cells):
        self.x_start = x_start
        self.x_end = x_end
        self.n_cells = n_cells
        self.n_faces = n_cells + 1
        self.face_x = np.linspace(x_start, x_end, self.n_faces)
        self.cell_x = 0.5 * (self.face_x[:-1] + self.face_x[1:])
        self.cell_distance = np.diff(self.cell_x)
        self.cell_size = np.diff(self.face_x)

    def __str__(self):
        cell_x = self.cell_x
        face_x = self.face_x
        return f"Mesh Information: \n" \
               f"X start: {self.x_start} \nX end: {self.x_end} \nCells no.: {self.n_cells} \n" \
               f"Cells co.: {cell_x} \nFaces co.: {face_x} \n"
