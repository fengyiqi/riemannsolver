import numpy as np
from ..config.domain import Domain
from .buffer import Buffer


class PrimitiveState(Buffer):
    def __init__(self):
        self.rho = np.zeros(Domain.cells_num)