import matplotlib
matplotlib.use('module://pyview.gui.mpl.backend')
from matplotlib.pyplot import *
from numpy import *

from pyview.lib.datacube import Datacube

gv.tomography1 = Datacube()
gv.tomography1.loadtxt("IQ tomography-11.par")
gv.tomography2 = Datacube()
gv.tomography2.loadtxt("IQ tomography-12.par")
gv.tomography3 = Datacube()
gv.tomography3.loadtxt("IQ tomography-13.par")
##

def makeMatrix(cube):
	n = sqrt(len(cube))
	m = zeros((n,n))
	for i in range(0,len(cube)):
		m[i%n,int(i/n)] = cube["px1"][i]
	return m

m1 = makeMatrix(gv.tomography1)
m2 = makeMatrix(gv.tomography2)
m3 = makeMatrix(gv.tomography3)

f = figure(2)
clf()
i = 1
subplot(1,3,1)
ylabel("Q quadrature amplitude [a.u.]")
for m in [m1,m2,m3]:
	subplot(1,3,i)
	xlabel("I quadrature amplitude [a.u.]")
	gray()
	imshow(m,aspect = 'auto',extent = (-1,1,-1,1),interpolation = 'bilinear')
	i+=1
show()
f.set_size_inches((20/2.54,6/2.54))
savefig("iq_tomographies.pdf")
show()
##
figure(1)
plot([1,2,3])
show()