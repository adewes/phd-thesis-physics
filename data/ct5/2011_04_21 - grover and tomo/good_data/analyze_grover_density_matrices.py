#Density matrix data:
#\thesis\data\ct5\2011_02_09 preparation of bell states\...

from numpy import *
from scipy.linalg import eigh,cholesky
import matplotlib
matplotlib.use('module://pyview.gui.mpl.backend_static')
from matplotlib.pyplot import *
import sys

import quantum.plotting
reload(sys.modules["quantum.plotting"])
from quantum.plotting import plotDensityMatricesContour

import quantum.qulib
reload(sys.modules["quantum.qulib"])
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
##Fit the density matrices from the spin data...
from pyview.lib.datacube import *

datacube = Datacube("iswap gate - maximum likelihood density matrices",dtype = complex128)
datacube.toDataManager()

spinMatrix = gv.spins

for i in range(0,len(gv.spins)):

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
	plotDensityMatricesContour([resultMatrix,initialMatrix],style="rectangle",annotate = True,labels=["00","01","10","11"])
	show()
	
##Simulate the Grover search algorithm

swap = matrix([[1,0,0,0],[0,0,-1j,0],[0,-1j,0,0],[0,0,0,1]])

step1 = tensor(roty(math.pi/2),roty(math.pi/2))

step2 = swap

step3 = lambda a,b:tensor(rotz(a*math.pi/2),rotz(b*math.pi/2))

step4 = swap

step5 = tensor(rotx(math.pi/2),rotx(math.pi/2))

steps = [step1,step2,step3,step4,step5]

cube = Datacube("simulated densityMatrices",dtype = complex128)
cube.toDataManager()
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
		toDatacube(finalState,cube)
		cube.commit()
		show()
##Plot the density matrices at different points during the algorithm
#You need to load the datacubes gv.densityMatrices and gv.simulatedDensityMatrices for this to work
import matplotlib.gridspec as gridspec
fig = figure(10)
clf()
fig.set_size_inches((12,10))
gs = gridspec.GridSpec(4, 5)
fidelityCube = Datacube("grover algorithm - fidelities")
fidelityCube.toDataManager()
for i in range(0,len(gv.densityMatrices)):
	if i % 5 == 1:
		continue
	if i % 5 >=1:
		a = -1
	else:
		a = 0
	if int(i/5) == 1:
		ax = subplot(gs[2,i % 5 + a])
	elif int(i/5) == 2:
		ax = subplot(gs[1,i % 5 + a])
	else:
		ax = subplot(gs[i/5,i % 5 + a])
	#subplot(4,5,i+1+a)
	densityMatrix = fromDatacube(gv.densityMatrices,i)
	simulatedDensityMatrix = fromDatacube(gv.simulatedDensityMatrices,i)
	if i == 0:
		annotate = True
	else:
		annotate = False
	plotDensityMatricesContour([densityMatrix,simulatedDensityMatrix],style="ellipse",annotate = annotate,labels=["00","01","10","11"],colors = ["red","black"],showOutline = [False,True])

	if (i % 5) < 4:
		a = Arrow(x = 3.7,y = 1.5,dx = 2.3,dy = 0,zorder = 10,width = 4,fc = (0.7,0.7,0.7),lw = 0)
		a.set_clip_on(False)
		ax.add_artist(a)

	fidelity = float(traceFidelity(densityMatrix,simulatedDensityMatrix))
	fidelityCube.set(i = i,fidelity = fidelity)
	fidelityCube.commit()
	title("$F_{tr}$ = %.2g %%" % (fidelity*100))
#	show()
#	time.sleep(1)
show()
##
savefig("grover algorithm - summary.pdf")
##
detector1 = matrix([[0.9515,1-0.8843],[1-0.9515,0.8843]])
detector2 = matrix([[0.9563,1-0.8737],[1-0.9563,0.8737]])
detector = tensor(detector1,detector2)

detectorReal = matrix(gv.groverSingleRunData.parameters()["qubit1"]["detectorFunction"])

figure(12)
clf()
plotDensityMatricesContour([detector,detectorReal],style="rectangle",annotate = annotate,labels=["00","01","10","11"])
show()

fig = figure(10)

rc('font',size = 10)
rc('axes', edgecolor=(0.5,0.5,0.5),facecolor = 'white')

for state in range(0,4):
	densityMatrix = fromDatacube(gv.densityMatrices,4+5*state)
	measuredProbs = map(lambda i:float(gv.groverSingleRunData.children()[state]["zzp"+i][0]),["00","10","01","11"])
	probs = matrix(map(lambda i:float(densityMatrix[i,i]),range(0,4)))
	if state == 1:
		ax = subplot(gs[2,4])
	elif state == 2:
		ax = subplot(gs[1,4])
	else:
		ax = subplot(gs[state,4])
	subplots_adjust(wspace = 0.4,hspace = 0.5,bottom = 0.2,top = 0.9)

	cla()

	ax.set_xlim(0,1)
	ax.barh([3.25,2.25,1.25,0.25],measuredProbs,color = 'red',lw = 1,height = 0.3)
	ax.barh([3.65,2.65,1.65,0.65],(probs*detector).tolist()[0],lw = 1,height = 0.1,color = 'blue',fill = True)
	ax.axhline(1,color = 'black',ls = 'dotted',zorder = -10)
	ax.axhline(2,color = 'black',ls = 'dotted',zorder = -10)
	ax.axhline(3,color = 'black',ls = 'dotted',zorder = -10)
	ax.axvline(0.5,color = 'black',ls = 'dashed',zorder = -10)

	ax.yaxis.set_ticks_position('none')
	xticks([0,0.25,0.5,0.75,1],["0","0.25","0.5","0.75","1"])
	if state != 3:
		setp(ax.get_xticklabels(),visible = False)
	yticks([3.5,2.5,1.5,0.5],["00","01","10","11"])
show()
savefig("grover algorithm - single run results.pdf")