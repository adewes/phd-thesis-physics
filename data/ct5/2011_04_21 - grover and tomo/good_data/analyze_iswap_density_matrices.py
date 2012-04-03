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
##	
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
##
from quantum.qulib import *
#statesLabels = ["|0>","|1>","(|0>-i|1>)","(|0>+|1>)"]
#initialStatesLabels = map(lambda x:statesLabels[x[0]]+statesLabels[x[1]],[(i,j) for i in range(0,4) for j in range(0,4)])
states = [gs,es,1/sqrt(2)*(gs-1j*es),1/sqrt(2)*(gs+es)]
initialStates = map(lambda x:adjoint(x)*x,map(lambda x:tensor(states[x[0]],states[x[1]]),[(i,j) for i in range(0,4) for j in range(0,4)]))
swap = 1/sqrt(2)*matrix([[sqrt(2),0,0,0],[0,1,-1j,0],[0,-1j,1,0],[0,0,0,sqrt(2)]])

outputStates = map(lambda x:swap*x*adjoint(swap),initialStates)

statesUnnormalized = [gs,es,(gs-1j*es),(gs+es)]
initialStatesUnnormalized = map(lambda x:array(tensor(statesUnnormalized[x[0]],statesUnnormalized[x[1]]))[0,:],[(i,j) for i in range(0,4) for j in range(0,4)])

initialStatesLabels = []
statesLabels = ["00","01","10","11"]
for state in initialStatesUnnormalized:
	label = ""
	first = True
	for i in range(0,len(state)):
		if state[i] != 0:
			if imag(state[i]) == 0:
				if real(state[i])>0:
					if not first:
						label+="+"
				else:
					label+="-"
			elif imag(state[i]) < 0:
				label+="-i"
			else:
				if not first:
					label+="+"
				label+="i"
			first = False
			label+="|%s>" % statesLabels[i]
	initialStatesLabels.append(label)
##
print initialStatesLabels
##
import matplotlib.gridspec as gridspec
fig = figure(10)
clf()
fig.set_size_inches((8,12))
gs = gridspec.GridSpec(4,4)
subplots_adjust(wspace = 0.2,hspace = 0.4,bottom = 0.2,top = 0.9)
rc('font',size = 10)
rc('axes', edgecolor=(0.5,0.5,0.5),facecolor = 'white')

offset = 0

for i in range(0,len(gv.densityMatrices)/2,2):
	ax = subplot(gs[int(i/4),(i) % 4])

	densityMatrix = fromDatacube(gv.densityMatrices,i+offset*2)

	if int(i/4) == 3 and i % 4 == 0:
		annotate = True
	else:
		annotate = False

	a = Arrow(x = 3.7,y = 1.5,dx = 0.8,dy = 0,zorder = 10,width = 2,fc = (0.7,0.7,0.7),lw = 0)
	a.set_clip_on(False)
	ax.add_artist(a)

	plotDensityMatricesContour([densityMatrix,initialStates[int(i/2)+offset]],style="ellipse",annotate = annotate,labels=["00","01","10","11"],colors = ["red","black"],showOutline = [False,True])
	fidelity = traceFidelity(densityMatrix,initialStates[int(i/2)+offset])
	title("$F_{tr}$ = %.2g %%" % (fidelity*100))

	xlabel("$%s$" % initialStatesLabels[int(i/2)+offset])

	ax = subplot(gs[int(i/4),(i) % 4+1])
	densityMatrix = fromDatacube(gv.densityMatrices,i+1+offset*2)

	plotDensityMatricesContour([densityMatrix,outputStates[int(i/2)+offset]],style="ellipse",annotate = False,labels=["00","01","10","11"],colors = ["red","black"],showOutline = [False,True])
	fidelity = traceFidelity(densityMatrix,outputStates[int(i/2)+offset])
	title("$F_{tr}$ = %.2g %%" % (fidelity*100))
	
#	title("F = %.2g %%" % (fidelity*100))
show()
##
savefig("process -matrices 1.pdf")
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
#fig.set_size_inches((12,12))
#clf()
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
#	ax = subplot(4,5,1+5*state+4)
	cla()
#	ax = fig.add_axes([0.,0,1,1])
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
##
densityMatrix = matrix(gv.data.parameters()["densityMatrix"])
figure(22)
clf()
plotDensityMatricesContour([densityMatrix],style="ellipse",annotate = False,labels=["00","01","10","11"],colors = ["red","black"],showOutline = [False,True])
show()