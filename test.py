import numpy as np
from riemannsolver.mesh import Mesh
from riemannsolver.initial_condition.shock_tube import ShockTubeInitialCondition

x_start, x_end = 0, 1
n_cells = 10

mesh = Mesh(x_start=x_start, x_end=x_end, n_cells=n_cells)
print(mesh)



init_rho = np.zeros(n_cells)
init_rho[mesh.cell_x < 0.5] = 1.0
init_rho[mesh.cell_x >= 0.5] = 0.1

init_vx = np.zeros(n_cells)

init_p = np.zeros(n_cells)
init_p[mesh.cell_x < 0.5] = 1.0
init_p[mesh.cell_x >= 0.5] = 0.125

shocktube = ShockTubeInitialCondition(mesh=mesh, rho=init_rho, vx=init_vx, p=init_p)

t_end = 0.01

print(shocktube)