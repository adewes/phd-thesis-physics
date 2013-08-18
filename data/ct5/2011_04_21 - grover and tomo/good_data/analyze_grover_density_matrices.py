#Density matrix data:
#\thesis\data\ct5\2011_02_09 preparation of bell states\...

from numpy import *
from scipy.linalg import eigh,cholesky
from quantum.plotting import plotDensityMatricesContour
import matplotlib
from matplotlib.pyplot import *
import sys

from pyview.lib.datacube import *
from quantum.qulib import *

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
##Fit the density matrices from the spin data...
from pyview.lib.datacube import *

densityMatrices = Datacube("grover - maximum likelihood density matrices",dtype = complex128)

if False:

	groverData = Datacube()
	groverData.loadtxt("Grover Search Algorithm-1")
	spinMatrix = Datacube()
	
	for child in groverData.children()[:-1]:
		spins = child.children()[0]
		print spins.rowAt(0)
		spinMatrix.set(**spins.rowAt(0))
		spinMatrix.commit()
	
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
		
		toDatacube(resultMatrix,densityMatrices)
		densityMatrices.commit()
		
		print i
	
		fig=figure(1)
		fig.set_size_inches((4,4))
		clf()
		plotDensityMatricesContour([resultMatrix,initialMatrix],style="rectangle",annotate = True,labels=["00","01","10","11"])
		show()
	densityMatrices.savetxt()
else:
	densityMatrices.loadtxt("grover - maximum likelihood density matrices-2")
	
##Simulate the Grover search algorithm

swap = matrix([[1,0,0,0],[0,0,-1j,0],[0,-1j,0,0],[0,0,0,1]])

step1 = tensor(roty(math.pi/2),roty(math.pi/2))

step2 = swap

step3 = lambda a,b:tensor(rotz(a*math.pi/2),rotz(b*math.pi/2))

step4 = swap

step5 = tensor(rotx(math.pi/2),rotx(math.pi/2))

steps = [step1,step2,step3,step4,step5]

simulatedDensityMatrices = Datacube("grover - simulated density matrices",dtype = complex128)

for signs in [(-1,-1),(1,-1),(-1,1),(1,1)]:
	sign_a = signs[0]
	sign_b = signs[1]
	for step in range(0,len(steps)):
		initialState = matrix([[1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]])
		alg = matrix(identity(4,dtype = complex128))
		for i in range(0,step+1):
			if i == 2:
				alg=steps[i](sign_a,sign_b)*alg
			else:
				alg=steps[i]*alg
		
		finalState = alg*initialState*adjoint(alg)
	
		fig=figure(2)
		fig.set_size_inches((4,4))
		clf()
		plotDensityMatricesContour([finalState],style="rectangle",annotate = True,labels=["00","01","10","11"])
		toDatacube(finalState,simulatedDensityMatrices)
		simulatedDensityMatrices.commit()
		show()
simulatedDensityMatrices.savetxt("grover algorithm - simulation")
##Plot the density matrices at different points during the algorithm
#You need to load the datacubes gv.densityMatrices and gv.simulatedDensityMatrices for this to work
import matplotlib.gridspec as gridspec
fig = figure(10)
clf()
fig.set_size_inches((12,10))
gs = gridspec.GridSpec(4, 5)
fidelityCube = Datacube("grover algorithm - fidelities")

for i in range(0,len(densityMatrices)):
	if i % 5 == 1:
		continue
	if i % 5 >=1:
		a = -1
	else:
		a = 0
	ax = subplot(gs[i/5,i % 5 + a])

	densityMatrix = fromDatacube(densityMatrices,i)
	simulatedDensityMatrix = fromDatacube(simulatedDensityMatrices,i)
	if i == 0:
		labels = ["00","01","10","11"]
	else:
		labels = []
	plotDensityMatricesContour([densityMatrix,simulatedDensityMatrix],style="ellipse",annotate = False,labels=labels,colors = ["red","black"],showOutline = [False,True])

	if (i % 5) < 4:
		a = Arrow(x = 3.7,y = 1.5,dx = 2.3,dy = 0,zorder = 10,width = 4,fc = (0.7,0.7,0.7),lw = 0)
		a.set_clip_on(False)
		ax.add_artist(a)

	fidelity = float(traceFidelity(densityMatrix,simulatedDensityMatrix))
	fidelityCube.set(i = i,fidelity = fidelity)
	fidelityCube.commit()
	title("$F_{tr}$ = %.2g %%" % (fidelity*100))

show()

savefig("grover algorithm - summary.pdf")
sys.stdin.readline()