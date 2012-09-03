#Density matrix data:
#\thesis\data\ct5\2011_02_09 preparation of bell states\...

from numpy import *
from scipy.linalg import eigh,cholesky
import matplotlib
matplotlib.use('module://pyview.gui.mpl.backend_static')
from matplotlib.pyplot import *
import sys

from quantum.plotting import plotDensityMatricesContour

from quantum.qulib import *

##
def generateDensityMatrix(params):
	dim = int(sqrt(len(params)+1))
	densityMatrix = matrix(zeros((dim,dim),dtype = complex128))
	c = 0
	for i in range(0,dim-1):
		densityMatrix[i,i] = abs(params[c])
		c+=1
	for i in range(1,dim):
		for j in range(0,i):
			densityMatrix[i,j]=params[c]+1j*params[c+1]
			c+=2
	
	s = 0
	for i in range(0,dim):
		s+= abs(adjoint(densityMatrix[:,i])*densityMatrix[:,i])

	if s > 1:
		s = 1
	
	densityMatrix[dim-1,dim-1] = sqrt(1-s)
	densityMatrix=densityMatrix*adjoint(densityMatrix)
	densityMatrix/=trace(densityMatrix)
	return densityMatrix

def toDatacube(densityMatrix,cube):
	d = densityMatrix.shape[0]
	for i in range(0,d):
		for j in range(0,d):
			cube.set(**{str(i)+str(j):densityMatrix[i,j]})

def fromDatacube(cube,row):
	d = int(sqrt(len(cube.names())))
	densityMatrix = matrix(zeros((d,d),dtype = complex128))
	for i in range(0,d):
		for j in range(0,d):
			densityMatrix[i,j] = cube[str(i)+str(j)][row]
	return densityMatrix
	
def renderMatrixPhysical(matrix):
	d = matrix.shape[0]
	(eigenvalues,eigenvectors) = eigh(matrix)
	for i in range(0,len(eigenvalues)):
		eigenvalues[i] = real(eigenvalues[i])
		if eigenvalues[i] < 0:
			eigenvalues[i] = 0.0001
	eigenvalues/=sum(eigenvalues)
	densityMatrix = eigenvectors*diag(eigenvalues)*adjoint(eigenvectors)
	return densityMatrix/trace(densityMatrix)

def parametrizeMatrix(matrix):
	d = matrix.shape[0]
	
	choleskyDecomposition = cholesky(matrix)
	params = []
	for i in range(0,d-1):
		params.append(float(choleskyDecomposition[i,i]))
	for i in range(1,d):
		for j in range(0,i):
			params.append(float(real(choleskyDecomposition[i,j])))
			params.append(float(imag(choleskyDecomposition[i,j])))
	return params

measurements = ["xx","xy","xz","yx","yy","yz","zx","zy","zz","xi","yi","zi","ix","iy","iz","ii"]
matrixMap = {"x":sigmax,"y":sigmay,"z":sigmaz,"i":idatom}
import itertools

def probability(params,measurementData,row):
	sum = 0
	dim = int(sqrt(len(params)+1))
	rho = generateDensityMatrix(params)
	for measurement in measurements:
		operator = tensor(matrixMap[measurement[0]],matrixMap[measurement[1]])
		value = trace(rho*operator)
		diff = value-measurementData[measurement][row]
		sum+=diff*diff/(1-value*value)
	return sum
##	
from pyview.lib.datacube import *

datacube = Datacube("iswap gate - maximum likelihood density matrices-16",dtype = complex128)


spinMatrix = Datacube()
spinMatrix.loadtxt("Quantum Process Tomography at 31 ns-16-spins-0")
spinMatrix.addChild(datacube)

for i in range(0,len(spinMatrix)):

	row = i

	initialMatrix = matrix(zeros((4,4),dtype = complex128))

	for m in measurements:
		initialMatrix+=spinMatrix[m][row]*tensor(matrixMap[m[0]],matrixMap[m[1]])

	initialMatrix/=4
	initialMatrix = renderMatrixPhysical(initialMatrix)

	print eigh(initialMatrix)[0]

	print "Parameters:",parametrizeMatrix(initialMatrix)

	reconstructedMatrix = generateDensityMatrix(parametrizeMatrix(initialMatrix))
	
	if not allclose(initialMatrix,reconstructedMatrix):
		print "Error parametrizing initial matrix!"

	import scipy.optimize
	
	result = scipy.optimize.fmin(probability,parametrizeMatrix(initialMatrix),args = (spinMatrix,row),maxiter = 1000,maxfun = 100000)

	resultMatrix = generateDensityMatrix(result)
	
	for a in range(0,4):
		for b in range(0,4):
			datacube.set(**{str(a)+str(b):resultMatrix[a,b]})
	
	datacube.commit()
	
	print trace(resultMatrix),eigh(resultMatrix)[0]

	fig=figure(1)
	fig.set_size_inches((4,4))
	clf()
	plotDensityMatricesContour([resultMatrix,initialMatrix],style="ellipse",annotate = False,labels=["00","01","10","11"])
	show()

datacube.savetxt()