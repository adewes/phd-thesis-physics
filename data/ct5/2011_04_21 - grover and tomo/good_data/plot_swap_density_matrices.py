
import sys
from numpy import *
from scipy.linalg import eigh,cholesky
import matplotlib
matplotlib.use('module://pyview.gui.mpl.backend_static')
from matplotlib.pyplot import *
from quantum.qulib import *
from quantum.plotting import plotDensityMatricesContour
from quantum.qulib import *
from pyview.lib.datacube import *

densityMatrices = Datacube()
densityMatrices.loadtxt("iswap gate - maximum likelihood density matrices-16")


def fromDatacube(cube,row,order = None):
	d = int(sqrt(len(cube.names())))
	densityMatrix = matrix(zeros((d,d),dtype = complex128))
	for i in range(0,d):
		for j in range(0,d):
			if order:
				ii = order[i]
				jj = order[j]
			else:
				ii = i
				jj = j
			densityMatrix[ii,jj] = cube[str(i)+str(j)][row]
	return densityMatrix
	
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

import matplotlib.gridspec as gridspec

fig = figure(10)
clf()
fig.set_size_inches((8,12))
gs = gridspec.GridSpec(4,4)
subplots_adjust(wspace = 0.2,hspace = 0.4,bottom = 0.2,top = 0.9)
rc('font',size = 10)
rc('axes', edgecolor=(0.5,0.5,0.5),facecolor = 'white')

offset = 8
order = [0,1,2,3]

for i in range(0,len(densityMatrices)/2,2):
	ax = subplot(gs[int(i/4),(i) % 4])

	densityMatrix = fromDatacube(densityMatrices,i+offset*2,order = order)

	labels = []
	if int(i/4) == 0 and i % 4 == 0:
		labels = ["00","01","10","11"]

	annotate = False
	

	a = Arrow(x = 3.7,y = 1.5,dx = 0.8,dy = 0,zorder = 10,width = 2,fc = (0.7,0.7,0.7),lw = 0)
	a.set_clip_on(False)
	ax.add_artist(a)
	
	figure(11,figsize = (4,4))
	clf()
	plotDensityMatricesContour([densityMatrix,initialStates[int(i/2)+offset]],style="ellipse",annotate = False,labels=["00","01","10","11"],colors = ["red","black"],showOutline = [False,True])
	savefig("input_matrices_%i.pdf" % ((i+offset*2)/2))
	clf()
	plotDensityMatricesContour([densityMatrix,outputStates[int(i/2)+offset]],style="ellipse",annotate = False,labels=["00","01","10","11"],colors = ["red","black"],showOutline = [False,True])
	savefig("output_matrices_%i.pdf" % ((i+offset*2)/2))
	figure(10)

	plotDensityMatricesContour([densityMatrix,initialStates[int(i/2)+offset]],style="ellipse",annotate = False,labels=labels,colors = ["red","black"],showOutline = [False,True])
	fidelity = traceFidelity(densityMatrix,initialStates[int(i/2)+offset])
	title("$F_{tr}$ = %.2g %%" % (fidelity*100))

	xlabel("$%s$" % initialStatesLabels[int(i/2)+offset])

	ax = subplot(gs[int(i/4),(i) % 4+1])
	densityMatrix = fromDatacube(densityMatrices,i+1+offset*2)

	figure(11,figsize = (4,4))
	clf()
	plotDensityMatricesContour([densityMatrix,outputStates[int(i/2)+offset]],style="ellipse",annotate = False,labels=["00","01","10","11"],colors = ["red","black"],showOutline = [False,True])
	savefig("output_matrices_%i.pdf" % ((i+offset*2)/2))
	figure(10)

	plotDensityMatricesContour([densityMatrix,outputStates[int(i/2)+offset]],style="ellipse",annotate = False,labels=[],colors = ["red","black"],showOutline = [False,True])
	fidelity = traceFidelity(densityMatrix,outputStates[int(i/2)+offset])
	title("$F_{tr}$ = %.2g %%" % (fidelity*100))
	
show()

savefig("process -matrices 2.pdf")
sys.stdin.readline()