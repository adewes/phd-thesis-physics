from config.startup import *
from numpy import *
from scipy import *
from numpy.linalg import *
from scripts.qulib import *
m1 = zeros((len(gv.survey),len(gv.survey.children()[0])))
m2 = zeros((len(gv.survey),len(gv.survey.children()[0])))
for i in range(0,len(gv.survey)):
	m1[i,:] = gv.survey.children()[i]["p1x"]
	m2[i,:] = gv.survey.children()[i]["px1"]
	
fs = gv.survey.children()[0]["f"]
##
figure("survey")
clf()


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
imshow(transpose(m1),aspect = 'auto',origin = 'lower',interpolation = 'nearest',extent = (gv.survey["flux"][0],gv.survey["flux"][-1],gv.survey.children()[0]["f"][0],gv.survey.children()[0]["f"][-1]))

plot(vs,ees[:,2]-ees[:,0],color = 'white',lw = 2,ls = 'solid')
plot(vs,ees[:,1]-ees[:,0],color = 'white',lw = 2,ls = 'solid')

xlim(1.26,1.29)
ylim(5.1,5.16)
title("Anticrossing spectroscopy - p1x")
xlabel("fluxline I voltage [V]")
ylabel("drive frequency [GHz]")

subplot(122)	
imshow(transpose(m2),aspect = 'auto',origin = 'lower',interpolation = 'nearest',extent = (gv.survey["flux"][0],gv.survey["flux"][-1],gv.survey.children()[0]["f"][0],gv.survey.children()[0]["f"][-1]))
title("Anticrossing spectroscopy - px1")
xlabel("fluxline I voltage [V]")
ylabel("drive frequency [GHz]")

plot(vs,ees[:,2]-ees[:,0],color = 'white',lw = 2,ls = 'solid')
plot(vs,ees[:,1]-ees[:,0],color = 'white',lw = 2,ls = 'solid')

xlim(1.26,1.29)
ylim(5.1,5.15)

figtext(0.02,0.02,gv.survey.filename()[:-4])
figtext(0.02,0.95,"$g = %g Mhz$\ncrosstalk = %g %%" % (g*1000,crosstalk * 100))
show()
##
from pyview.helpers.datamanager import DataManager

dataManager = DataManager()

fit = Datacube("fit")
dataManager.addDatacube(fit)

for i in range(0,len(gv.survey)):

	fit.set(i= i,flux = gv.survey["flux"][i])

	j = argmin(abs(vs-gv.survey["flux"][i]))
	fqb1 = real(ees[j,2]-ees[j,0])
	fqb2 = real(ees[j,1]-ees[j,0])
	print gv.survey["flux"][i],vs[j]
	import scipy.optimize
	import numpy.linalg
	fitfunc = lambda p, x: 1./math.pi*p[0]/((x-p[1])*(x-p[1])/p[3]/p[3]+1)+p[2]+1./math.pi*p[4]/((x-p[5])*(x-p[5])/p[6]/p[6]+1) # Target function
	errfunc = lambda p, x, y: fitfunc(p, x) - y # Distance to the target function
	ps = [0.4,fqb1,0.1,0.002,0.3,fqb2,0.002]
	p2,success = scipy.optimize.leastsq(errfunc, array(ps), args=(array(fs), array(m1[i])))
	
	fit.set(fqb1 = p2[1],fqb2 = p2[5])
	fit.commit()
	
#	figure("single spectro")
#	cla()
#	plot(fs,m1[i,:])
#	plot(fs,fitfunc(p2,fs))
#	show()

print real(ees[j,2]-ees[j,0])

##
figure("fit of anticrossing")
cla()
plot(fit["flux"][20:40],fit["fqb1"][20:40],'co')
plot(fit["flux"][20:40],fit["fqb2"][20:40],'co')
plot(vs,map(lambda flux:calculate_fqb1(flux,0.0082),vs),color = 'black',lw = 2,ls = 'solid')
plot(vs,map(lambda flux:calculate_fqb2(flux,0.0082),vs),color = 'red',lw = 2,ls = 'solid')
xlim(1.27,1.28)
ylim(5.105,5.14)
show()