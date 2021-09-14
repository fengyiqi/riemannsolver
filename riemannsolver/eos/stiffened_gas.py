from .eos import EquationOfState
import numpy as np

_gamma = 1.4
_A = 0
_B = 0
_rho0 = 0
_mu_shear = 0
_mu_bulk = 0


class StiffenedGas(EquationOfState):
    def __init__(self,
                 gamma=_gamma,
                 A=_A,
                 B=_B,
                 rho0=_rho0,
                 mu_shear=_mu_shear,
                 mu_bulk=_mu_bulk
                 ):
        self.gamma = gamma
        self.A = A
        self.B = B
        self.rho0 = rho0
        self.mu_shear = mu_shear
        self.mu_bulk = mu_bulk

    def get_pressure(self, rho, rhoU, p):
        pressure = -self.gamma * self.B
        pressure += (self.gamma - 1.0) * (self.get_energy(rho, rhoU, p) - 0.5 * rhoU**2 / rho)

    def get_speed_of_sound(self, rho, p):
        return np.sqrt(self.gamma * (p + self.B) / rho)

    def get_energy(self, rho, rhoU, p):
        energy = p + self.gamma * self.B
        energy /= (self.gamma - 1.0) + (0.5 * rhoU ** 2) / rho
        return energy
