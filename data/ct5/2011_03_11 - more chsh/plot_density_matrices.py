import sys
from qulib import *
sys.path.append(r"c:\labo\python")
from qubit_setup.scripts.state_tomography.plot_density_matrix import *

rho = matrix(zeros((4,4),dtype = complex128))

for i in range(0,4):
	for j in range(0,4):
		rho[i,j] = gv.densityMatrices[str(i)+str(j)][3]
cla()
plotDensityMatrix(rho)
show()