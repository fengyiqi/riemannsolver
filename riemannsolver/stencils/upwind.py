from ..boundary_condition import symmetry


def first_order(cell_values, velocity: bool):
    extend_cell_values = symmetry(cell_values=cell_values, velocity=velocity)
    WL = extend_cell_values[:-1]
    WR = extend_cell_values[1:]
    # print(WL)
    return WL, WR
