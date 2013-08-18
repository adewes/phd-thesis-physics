#Density matrix data:
#\thesis\data\ct5\2011_02_09 preparation of bell states\...

from numpy import *
from scipy.linalg import eigh,cholesky
import sys

from quantum.plotting import plotDensityMatricesContour
from matplotlib.pylab import *
from pyview.lib.datacube import *
from quantum.qulib import *
from pyview.lib.datacube import *

spinMatrix = Datacube()
spinMatrix.loadtxt("Quantum Process Tomography at 31 ns-16-spins-0")

figure(1,figsize = (6,3))
clf()
indices = ["xi","yi","zi","ix","iy","iz","xx","xy","xz","yx","yy","yz","zx","zy","zz"]
for i in range(0,len(spinMatrix)):
#	ax = subplot(8,4,i)
#	a = Arrow(x = 3.7,y = 1.5,dx = 0.8,dy = 0,zorder = 10,width = 2,fc = (0.7,0.7,0.7),lw = 0)
#	a.set_clip_on(False)
#	ax.add_artist(a)
	clf()
	bar(range(0,15),map(lambda x:spinMatrix[x][i],indices),color = ["red"]*3+["green"]*3+["blue"]*9)
	xticks(arange(0,15)+0.5,map(lambda x:x.upper(),indices),rotation = -45)
	yticks([-1,-0.5,0,0.5,1])
	xlim(-0.2,15)
	ylim(-1.1,1.1)
	axhline(1,ls = '--',color = 'grey')
	axhline(-1,ls = '--',color = 'grey')
	show()
	savefig("pauli_set_%i.pdf" % i)
sys.stdin.readline()