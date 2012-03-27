from numpy import *
from numpy.linalg import *
from scipy import *

def adjoint(m):
	return m.conj().transpose()

def loadDensityMatrix(datacube,row):
	m = matrix(zeros((4,4),dtype = complex128))
	for i in range(0,4):
		for j in range(0,4):
			m[i,j] = datacube[str(i)+str(j)][row]
	return m

def sqrtm(A):
	(eigenvals,eigenvecs) = eigh(A)
	return (eigenvecs)*diag(sqrt(eigenvals))*adjoint(eigenvecs)

def quantumFidelity(measuredRho,targetRho):
	return trace(sqrtm(sqrtm(measuredRho)*targetRho*sqrtm(measuredRho)))
##
densityMatrices = gv.groverAlgorithm.children()[-1]
for i in range(0,20):
	child = gv.groverAlgorithm.children()[i]
	if "targetRho" in child.parameters():
		ma = matrix(child.parameters()["targetRho"])
		mb = loadDensityMatrix(densityMatrices,i)
		print int(densityMatrices["state"][i]),int(densityMatrices["step"][i]),":",abs(quantumFidelity(ma,mb))
##
print gv.state1.parameters()["state"]