import numpy as np
from ..config.domain import Domain
from .buffer import Buffer


class ConservativeState(Buffer):
    def __init__(self):
        self.density = np.zeros(Domain.cells_num)
        self.momentum = np.zeros(Domain.cells_num)
