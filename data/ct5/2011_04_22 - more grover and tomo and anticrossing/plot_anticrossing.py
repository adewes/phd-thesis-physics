import matplotlib
matplotlib.use('module://pyview.gui.mpl.backend_static')
from matplotlib.pyplot import *
from numpy import *
from scipy import *
from numpy.linalg import *
from quantum.qulib import *
from pyview.lib.datacube import *

survey = Datacube()
survey.loadtxt("Spectroscopy Survey - qubit1-7")

figure(10,figsize = (8,4))
clf()
m1 = zeros((len(survey),len(survey.children()[0])))
m2 = zeros((len(survey),len(survey.children()[0])))
for i in range(0,len(survey)):
	m1[i,:] = survey.children()[i]["p1x"]
	m2[i,:] = survey.children()[i]["px1"]

H_1 = lambda f1:tensor(matrix([[-f1/2.,0],[0,f1/2.]]),idatom)
H_2 = lambda f2:tensor(idatom,matrix([[-f2/2.,0],[0,f2/2.]]))

H_total = lambda f1,f2,g:H_1(f1)+H_2(f2)+matrix([[0,0,0,0],[0,0,g/2.,0],[0,g/2.,0,0],[0,0,0,0]],dtype = complex128)

v2 = 0
g = 0.0082
crosstalk = 0.02

f1 = lambda v1: 5.16+(v1-1.26)*(5.101-5.16)/(1.285-1.26)
f2 = lambda v1: 5.1258+(f1(v1)-f1(1.26))*crosstalk

vs = linspace(1.26,1.31,100)

ees = zeros((len(vs),4),dtype = complex128)

for i in range(0,len(vs)):

	ff1 = f1(vs[i])
	ff2 = f2(vs[i])

	ees[i,:] = eigh(H_total(ff1,ff2,g))[0]
	
def calculate_fqb1(flux,g):
	ff1 = f1(flux)
	ff2 = f2(flux)
	ees = eigh(H_total(ff1,ff2,g))[0]
	return ees[2]-ees[0]

def calculate_fqb2(flux,g):
	ff1 = f1(flux)
	ff2 = f2(flux)
	ees = eigh(H_total(ff1,ff2,g))[0]
	return ees[1]-ees[0]

subplot(121)	
imshow(transpose(m1),aspect = 'auto',origin = 'lower',interpolation = 'nearest',extent = (survey["flux"][0],survey["flux"][-1],survey.children()[0]["f"][0],survey.children()[0]["f"][-1]))

#plot(vs,ees[:,2]-ees[:,0],color = 'red',lw = 2,ls = 'dashed')
#plot(vs,ees[:,1]-ees[:,0],color = 'red',lw = 2,ls = 'dashed')

xlim(1.26,1.29)
ylim(5.1,5.15)
title("$p(|1*>)$")
xlabel("fluxline I voltage")
ylabel("drive frequency [GHz]")
xticks([])
subplot(122)	

imshow(transpose(m2),aspect = 'auto',origin = 'lower',interpolation = 'nearest',extent = (survey["flux"][0],survey["flux"][-1],survey.children()[0]["f"][0],survey.children()[0]["f"][-1]))

#plot(vs,ees[:,2]-ees[:,0],color = 'red',lw = 2,ls = 'dashed')
#plot(vs,ees[:,1]-ees[:,0],color = 'red',lw = 2,ls = 'dashed')

xlim(1.26,1.29)
ylim(5.1,5.15)
xticks([])
title("$p(|*1>)$")
xlabel("fluxline II voltage")
#ylabel("drive frequency [GHz]")
#figtext(0.02,0.02,survey.filename()[:-4])
show()

savefig("qubits - anticrossing.png",dpi = 300)

import sys
sys.stdin.readline()
