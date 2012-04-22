#Density matrix data:
#\thesis\data\ct5\2011_02_09 preparation of bell states\...

from numpy import matrix
import matplotlib
matplotlib.use('module://pyview.gui.mpl.backend_static')
from matplotlib.pyplot import *
import sys

import quantum.plotting
reload(sys.modules["quantum.plotting"])
from quantum.plotting import plotDensityMatricesContour

import quantum.qulib
reload(sys.modules["quantum.qulib"])
from quantum.qulib import stateFidelity,traceFidelity

psiPlusMatrixIdeal = matrix([[0.5,0,0,0.5],[0,0,0,0],[0,0,0,0],[0.5,0,0,0.5]])
psiMinusMatrixIdeal = matrix([[0.5,0,0,-0.5],[0,0,0,0],[0,0,0,0],[-0.5,0,0,0.5]])

phiPlusMatrixIdeal = matrix([[0.0,0,0,0.0],[0,0.5,0.5,0],[0,0.5,0.5,0],[0,0,0,0]])
phiMinusMatrixIdeal = matrix([[0,0,0,0],[0,0.5,-0.5,0],[0,-0.5,0.5,0],[0,0,0,0]])

import cmath

def c(r,phi): 
	return r*cmath.exp(1j*phi/180.0*math.pi)

print c(0.4,-70)

phiMinusMatrix = matrix([[0.1,c(0.03,-70),c(0.04,180),c(0,0)],[c(0.03,66),0.46,c(0.45,200),0],[c(0.04,180),c(0.45,160),0.44,0],[0,0,0,0]])

phiPlusMatrix = matrix([[0.11,c(0.05,77),c(0.04,140),0.01],[c(0.05,-80),0.43,c(0.44,13),0.02],[c(0.04,132),c(0.44,-13),0.46,0.03],[0.01,0.02,0.03,0]])

from cmath import *

for i in range(1,4):
	for j in range(0,i):
		for m in [phiMinusMatrix,phiPlusMatrix]:
			m[j,i] = m[i,j].conjugate()

psiMinusMatrix = matrix([[(0.46897871228514415+0j), (0.0787538679534797+0j), (-0.01674925247855+0.00172926959478613j), (-0.4297743574491255-0.020974501340607927j)], [(0.0787538679534797+0j), (0.013224847002998141+0j), (0.03992324135304936+0j), (0.04211084712077284+0.016900339646178042j)], [(-0.01674925247855-0.00172926959478613j), (0.03992324135304936+0j), (0.12052050203473001+0j), (0.051750707321192996-0.0020741618904280444j)], [(-0.4297743574491255+0.020974501340607927j), (0.04211084712077284-0.016900339646178042j), (0.051750707321192996+0.0020741618904280444j), (0.39727593867712774+0j)]])

psiPlusMatrix = matrix([[(0.47356299048313577+0j), (0.04603334696364297+0j), (-0.04479988764319459-0.009609979426587522j), (0.40492025330865916+0.07908492432292454j)], [(0.04603334696364297+0j), (0.004474735305039848+0j), (0.026107022049126117+0j), (0.03683472221169762-0.005920236771060207j)], [(-0.04479988764319459+0.009609979426587522j), (0.026107022049126117+0j), (0.15231662965760334+0j), (-0.035290388800884955+0.013034753743398401j)], [(0.40492025330865916-0.07908492432292454j), (0.03683472221169762+0.005920236771060207j), (-0.035290388800884955-0.013034753743398401j), (0.3696456445542211+0j)]])

matrices = [(phiPlusMatrix,phiPlusMatrixIdeal),(phiMinusMatrix,phiMinusMatrixIdeal),(psiPlusMatrix,psiPlusMatrixIdeal),(psiMinusMatrix,psiMinusMatrixIdeal)]
fig=figure(1)
fig.set_size_inches((8,3))
clf()

i = 1
for matrixPair in matrices:
	subplot(1,4,i)
	if i == 1:
		annotate = True
	else:
		annotate = False
	plotDensityMatricesContour([matrixPair[0],matrixPair[1]],style="ellipse",annotate = annotate,labels=["00","01","10","11"],colors = ["red","black"],showOutline = [False,True])
	title("$F_{tr}$ = %.2g %%" % (traceFidelity(matrixPair[0],matrixPair[1])*100))
	show()
	i+=1
savefig("bell matrices.pdf")

