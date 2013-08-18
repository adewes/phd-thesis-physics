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

labels = ["xx", "xy", "xz", "xi", "yx", "yy", "yz", "yi", "zx", "zy", "zz", \
"zi", "ix", "iy", "iz", "ii"]
spins = [0, 1, 0, 0, -1, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 1]

figure(1,figsize = (6,3))
clf()
indices = ["xi","yi","zi","ix","iy","iz","xx","xy","xz","yx","yy","yz","zx","zy","zz"]

clf()
bar(range(0,15),map(lambda x:spins[labels.index(x)],indices),color = ["red"]*3+["green"]*3+["blue"]*9)
xticks(arange(0,15)+0.5,map(lambda x:x.upper(),indices),rotation = -45)
yticks([-1,-0.5,0,0.5,1])
xlim(-0.2,15)
ylim(-1.1,1.1)
axhline(1,ls = '--',color = 'grey')
axhline(-1,ls = '--',color = 'grey')
show()
savefig("pauli_set_example.png")

sys.stdin.readline()