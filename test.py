import numpy as np
from riemannsolver.mesh import Mesh
from riemannsolver.initial_condition.shock_tube import ShockTubeInitialCondition
from riemannsolver.plot.plot2D import plot2D
from riemannsolver.solvers.advance import advance
from riemannsolver.eos.stiffened_gas import StiffenedGas
from riemannsolver.solvers.riemann_solvers.simple import SimpleFluxSolver


x_start, x_end = 0, 1
n_cells = 100

mesh = Mesh(x_start=x_start, x_end=x_end, n_cells=n_cells)




init_rho = np.zeros(n_cells)
init_rho[mesh.cell_x < 0.5] = 1.0
init_rho[mesh.cell_x >= 0.5] = 0.1

init_vx = np.zeros(n_cells)

init_p = np.zeros(n_cells)
init_p[mesh.cell_x < 0.5] = 1.0
init_p[mesh.cell_x >= 0.5] = 0.125

shocktube = ShockTubeInitialCondition(mesh=mesh, rho=init_rho, vx=init_vx, p=init_p)

t_end = 0.0017
# plot2D(mesh.cell_x, [init_rho, init_vx, init_p], label=["Density", "Velocity", "Pressure"])
print(mesh.cell_size)

out = advance(t_span=(0, t_end), riemann_solver=SimpleFluxSolver, time_interator="RK45", mesh=mesh, init_cond=shocktube)
# print(mesh.cell_x, out.y.shape, out.t.shape)
plot2D(mesh.cell_x, out.y[:100, -1], label="rho")