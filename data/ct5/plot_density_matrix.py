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
from quantum.qulib import stateFidelity

psiPlusMatrixIdeal = matrix([[0.5,0,0,0.5],[0,0,0,0],[0,0,0,0],[0.5,0,0,0.5]])
psiMinusMatrixIdeal = matrix([[0.5,0,0,-0.5],[0,0,0,0],[0,0,0,0],[-0.5,0,0,0.5]])

psiMinusMatrix = matrix([[(0.46897871228514415+0j), (0.0787538679534797+0j), (-0.01674925247855+0.00172926959478613j), (-0.4297743574491255-0.020974501340607927j)], [(0.0787538679534797+0j), (0.013224847002998141+0j), (0.03992324135304936+0j), (0.04211084712077284+0.016900339646178042j)], [(-0.01674925247855-0.00172926959478613j), (0.03992324135304936+0j), (0.12052050203473001+0j), (0.051750707321192996-0.0020741618904280444j)], [(-0.4297743574491255+0.020974501340607927j), (0.04211084712077284-0.016900339646178042j), (0.051750707321192996+0.0020741618904280444j), (0.39727593867712774+0j)]])

psiPlusMatrix = matrix([[(0.47356299048313577+0j), (0.04603334696364297+0j), (-0.04479988764319459-0.009609979426587522j), (0.40492025330865916+0.07908492432292454j)], [(0.04603334696364297+0j), (0.004474735305039848+0j), (0.026107022049126117+0j), (0.03683472221169762-0.005920236771060207j)], [(-0.04479988764319459+0.009609979426587522j), (0.026107022049126117+0j), (0.15231662965760334+0j), (-0.035290388800884955+0.013034753743398401j)], [(0.40492025330865916-0.07908492432292454j), (0.03683472221169762+0.005920236771060207j), (-0.035290388800884955-0.013034753743398401j), (0.3696456445542211+0j)]])

fig=figure(1)
fig.set_size_inches((4,4))
clf()
plotDensityMatricesContour([psiMinusMatrix,psiMinusMatrixIdeal],style="rectangle",annotate = True,labels=["00","01","10","11"])
savefig("psi_minus.pdf")
fig=figure(2)
fig.set_size_inches((4,4))
clf()
plotDensityMatricesContour([psiPlusMatrix,psiPlusMatrixIdeal],style="rectangle",annotate = True,labels=["00","01","10","11"])
savefig("psi_plus.pdf")
##
print stateFidelity(psiPlusMatrix,psiPlusMatrixIdeal)
print stateFidelity(psiMinusMatrix,psiMinusMatrixIdeal)