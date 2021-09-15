from .flux_solver import FluxSolver
from ...stencils.upwind import first_order
import numpy as np
from ...eos.stiffened_gas import StiffenedGas
from ...mesh import Mesh


class SimpleFluxSolver(FluxSolver):
    def __init__(self, mesh: Mesh):
        self.dx = mesh.cell_size
        self.n = mesh.n_cells

    #     self.WL_rho, self.WR_rho = first_order(rho, velocity=False)
    #     self.WL_rhoU, self.WR_rhoU = first_order(rhoU, velocity=True)
    #     self.WL_rhoE, self.WR_rhoE = first_order(rhoE, velocity=False)
    #     # self.WL_E, self.WR_E = self.WL_rhoE / self.WL_rho, self.WR_rhoE / self.WR_rho
    #     self.WL_p, self.WR_p = first_order(StiffenedGas().get_pressure(rho, rhoU, rhoE / rho), velocity=False)
    #     self.WL = np.vstack((self.WL_rho, self.WL_rhoU, self.WL_rhoE))
    # self.WR = np.vstack((self.WR_rho, self.WR_rhoU, self.WR_rhoE))

    def get_rhs(self, x):
        rho_ = x[0]
        rhoU_ = x[1]
        rhoE_ = x[2]

        W = self.get_states(rho_, rhoU_, rhoE_)
        rho, rhoU, rhoE, p = W[0], W[1], W[2], W[3]

        face_fluxes = np.zeros_like(W)
        face_fluxes[0, :] = rhoU
        face_fluxes[1, :] = rhoU * rhoU / rho + p
        face_fluxes[2, :] = rhoE * rhoU / rho + p * rhoU / rho
        # print(face_fluxes)
        time_derive = (1 / self.dx[0]) * (face_fluxes[:, :-1] - face_fluxes[:, 1:])

        return time_derive.flatten()

    @staticmethod
    def get_states(rho, rhoU, rhoE):
        WL_rho, WR_rho = first_order(rho, velocity=False)
        WL_rhoU, WR_rhoU = first_order(rhoU, velocity=True)
        WL_rhoE, WR_rhoE = first_order(rhoE, velocity=False)

        WL_p, WR_p = first_order(StiffenedGas().get_pressure(rho, rhoU, rhoE / rho), velocity=False)
        WL = np.vstack((WL_rho, WL_rhoU, WL_rhoE, WL_p))
        WR = np.vstack((WR_rho, WR_rhoU, WR_rhoE, WR_p))
        # print(WL)
        return 0.5 * WL + 0.5 * WR

    def solve(self, t, x):
        print(t)
        x_ = np.vstack((x[:self.n], x[self.n:2 * self.n], x[2 * self.n:3 * self.n], x[3 * self.n:]))

        return self.get_rhs(x_)
