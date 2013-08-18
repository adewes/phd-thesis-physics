from numpy import *
from scipy.linalg import eigh,cholesky
import matplotlib
matplotlib.use('module://pyview.gui.mpl.backend_static')
from matplotlib.pyplot import *
import sys

import quantum.plotting
reload(sys.modules["quantum.plotting"])
from quantum.plotting import plotDensityMatricesContour
from pyview.lib.datacube import *
import quantum.qulib
reload(sys.modules["quantum.qulib"])
from quantum.qulib import *

densityMatrices = Datacube()
groverSingleRunData = Datacube()

densityMatrices.loadtxt("grover - maximum likelihood density matrices-2")
groverSingleRunData.loadtxt("Grover Search Algorithm")


def fromDatacube(cube,row):
	d = int(sqrt(len(cube.names())))
	densityMatrix = matrix(zeros((d,d),dtype = complex128))
	for i in range(0,d):
		for j in range(0,d):
			densityMatrix[i,j] = cube[str(i)+str(j)][row]
	return densityMatrix


detector1 = matrix([[0.9515,1-0.8843],[1-0.9515,0.8843]])
detector2 = matrix([[0.9563,1-0.8737],[1-0.9563,0.8737]])
detector = tensor(detector1,detector2)

detectorReal = matrix(groverSingleRunData.parameters()["qubit1"]["detectorFunction"])

import matplotlib.gridspec as gridspec

figure(12)
clf()
plotDensityMatricesContour([detector,detectorReal],style="rectangle",annotate = annotate,labels=["00","01","10","11"])
show()

fig = figure(10)
subplot(441)
rc('font',size = 12)
rc('axes', edgecolor=(0.5,0.5,0.5),facecolor = 'white')

fig.set_size_inches((12,3))
gs = gridspec.GridSpec(1, 4)

for state in range(0,4):
	densityMatrix = fromDatacube(densityMatrices,4+5*state)
        print densityMatrix
	measuredProbs = map(lambda i:float(groverSingleRunData.children()[state]["zzp"+i][0]),["00","01","10","11"])
	probs = matrix(map(lambda i:float(densityMatrix[i,i]),range(0,4)))
	ax = subplot(gs[0,state])
	subplots_adjust(wspace = 0.4,hspace = 0.5,bottom = 0.2,top = 0.9)

	cla()

	ax.set_xlim(0,1)
        
        print "Probability sum:",sum(probs*transpose(detectorReal))
        print "Probability sum:",sum(probs*transpose(detector))
        print "Probability sum:",sum(measuredProbs)
        
	ax.barh([3.25,2.25,1.25,0.25],measuredProbs,color = 'red',lw = 1,height = 0.3)
	ax.barh([3.65,2.65,1.65,0.65],(probs*transpose(detectorReal)).tolist()[0],lw = 1,height = 0.1,color = 'blue',fill = True)
#	ax.barh([3.0,2.0,1.0,0.0],(probs*transpose(detector)).tolist()[0],lw = 1,height = 0.1,color = 'green',fill = True)
	ax.axhline(1,color = 'black',ls = 'dotted',zorder = -10)
	ax.axhline(2,color = 'black',ls = 'dotted',zorder = -10)
	ax.axhline(3,color = 'black',ls = 'dotted',zorder = -10)
	ax.axvline(0.5,color = 'black',ls = 'dashed',zorder = -10)

	ax.yaxis.set_ticks_position('none')
	xticks([0,0.25,0.5,0.75,1],["0","0.25","0.5","0.75","1"])
#	if state != 3:
#		setp(ax.get_xticklabels(),visible = False)
	yticks([3.5,2.5,1.5,0.5],["00","01","10","11"])
show()
savefig("grover algorithm - single run probabilities.pdf")

import sys
sys.stdin.readline()