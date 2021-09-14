from .initial_condition import InitialCondition
from ..mesh import Mesh
import numpy as np
from ..eos.stiffened_gas import StiffenedGas


class ShockTubeInitialCondition(InitialCondition):
    def __init__(self, mesh: Mesh, rho, vx, p):
        self.rho = rho
        self.vx = vx
        self.p = p
        self.rhoU = rho * vx
        self.E = StiffenedGas().get_energy(rho, self.rhoU, p)
        self.rhoE = rho * self.E

    def __str__(self):
        return f"Initial Conditon: \n" \
               f"- Primitive Variables: \n" \
               f"\tDensity:\t{self.rho} \n" \
               f"\tVelocityX:\t{self.vx} \n" \
               f"\tPressure:\t{self.p} \n" \
               f"- Conservative Variables: \n" \
               f"\tDensity:\t{self.rho} \n" \
               f"\tMomentumX:\t{self.rhoU} \n" \
               f"\tTotal E:\t{self.rhoE} \n"

    def set_rho(self, density):
        self.rho = density

    def set_vx(self, velocityX):
        self.vx = velocityX

    def set_p(self, pressure):
        self.p = pressure

    def set_initial_condition(self, rho, vx, p):
        self.rho = rho
        self.vx = vx
        self.p = p
