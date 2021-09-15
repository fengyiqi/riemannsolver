from ..initial_condition.initial_condition import InitialCondition
from .riemann_solvers.simple import SimpleFluxSolver
from ..mesh import Mesh
import scipy.integrate as integrate
import numpy as np

def advance(
        t_span,
        riemann_solver,
        time_interator: str,
        init_cond: InitialCondition,
        mesh: Mesh
):
    solver = riemann_solver(mesh).solve
    X0 = np.hstack((init_cond.rho, init_cond.rhoU, init_cond.rhoE, init_cond.p))
    out = integrate.solve_ivp(fun=lambda t, x: solver(t, x), t_span=t_span, y0=X0, method=time_interator)
    return out