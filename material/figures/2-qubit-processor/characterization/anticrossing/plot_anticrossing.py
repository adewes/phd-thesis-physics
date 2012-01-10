#!/usr/bin/python
import matplotlib

matplotlib.use('module://pyview.gui.mpl.backend')

from pyview.lib.datacube import Datacube
from matplotlib.pyplot import *

from phdthesis.config.params import params
from phdthesis.config.matplotlib.rcparams import *

import sys

titleString = "2 Qubit Anticrossing"
outputFilename = "anticrossing"
dataFile = r"data/Spectroscopy Survey - qubit1-7.txt"

print "Loading data..."

datacube = Datacube()
datacube.loadtxt(dataFile)

##

from numpy import *
from numpy.linalg import *

m1 = zeros((len(datacube.children()[0]),len(datacube)))
m2 = zeros((len(datacube.children()[0]),len(datacube)))

for i,child in enumerate(datacube.children()):
	m1[:,i] = child["p1x"] 
	m2[:,i] = child["px1"] 

##Generate a model of the qubit anticrossing

def tensor(a,b):
	return kron(b,a)

idatom = matrix(eye(2))

H_1 = lambda f1:tensor(matrix([[-f1/2.,0],[0,f1/2.]]),idatom)
H_2 = lambda f2:tensor(idatom,matrix([[-f2/2.,0],[0,f2/2.]]))

H_total = lambda f1,f2,g:H_1(f1)+H_2(f2)+matrix([[0,0,0,0],[0,0,g/2.,0],[0,g/2.,0,0],[0,0,0,0]],dtype = complex128)

v2 = 0
g = 0.009
crosstalk = 0.02

f1 = lambda v1: 5.16+(v1-1.26)*(5.101-5.16)/(1.285-1.26)
f2 = lambda v1: 5.1258+(f1(v1)-f1(1.26))*crosstalk

vs = linspace(1.26,1.31,100)

ees = zeros((len(vs),4),dtype = complex128)

for i in range(0,len(vs)):

	ff1 = f1(vs[i])
	ff2 = f2(vs[i])

	ees[i,:] = eigh(H_total(ff1,ff2,g))[0]
	
def fqb1(flux,g):
	ff1 = f1(flux)
	ff2 = f2(flux)
	ees = eigh(H_total(ff1,ff2,g))[0]
	return ees[2]-ees[0]

def fqb2(flux,g):
	ff1 = f1(flux)
	ff2 = f2(flux)
	ees = eigh(H_total(ff1,ff2,g))[0]
	return ees[1]-ees[0]
	

##
print "Generating figure \"%s\"" % titleString

matplotlib.rc("xtick", direction="out")
matplotlib.rc("ytick", direction="out")
matplotlib.rc("font",size = 10)

f = figure(1)
f.set_size_inches((params["figureStandardWidth"],params["figureStandardHeight"]))
clf()

subplot(121)
imshow(m1,origin = 'upper',aspect = 'auto',interpolation = 'nearest',extent = (datacube["flux"][0],datacube["flux"][-1],datacube.children()[0]["f"][-1],datacube.children()[0]["f"][0]))

plot(vs,ees[:,2]-ees[:,0],color = 'black',lw = 2,ls = 'dashed')
plot(vs,ees[:,1]-ees[:,0],color = 'black',lw = 2,ls = 'dashed')
xticks(arange(1.271,1.279,0.004))

xlim(1.27,1.28)
ylim(5.1,5.15)
title("Qubit 1 - Switching Probability")
xlabel("$V_{fl1}$ [V]")
ylabel("$f_{dr}$ [GHz]")

subplot(122)
imshow(m2,origin = 'upper',aspect = 'auto',interpolation = 'nearest',extent = (datacube["flux"][0],datacube["flux"][-1],datacube.children()[0]["f"][-1],datacube.children()[0]["f"][0]))

plot(vs,ees[:,2]-ees[:,0],color = 'black',lw = 2,ls = 'dashed')
plot(vs,ees[:,1]-ees[:,0],color = 'black',lw = 2,ls = 'dashed')
xticks(arange(1.271,1.279,0.004))

xlim(1.27,1.28)
ylim(5.1,5.15)
title("Qubit 2 - Switching Probability")
xlabel("$V_{fl1}$ [V]")

for outputFormat in params["figureOutputFormats"]:
    filename = "%s.%s" % (outputFilename,outputFormat)
    print "Saving figure as \"%s\"" % filename
    savefig(filename)

if "-i" in sys.argv:
    show()
    print "[press any key to exit]"
    sys.stdin.readline()
show()
print "Done..." 
##
xticks(arange(1.271,1.279,0.004))
show()