import matplotlib
matplotlib.use('module://pyview.gui.mpl.backend')
from matplotlib.pyplot import *
from numpy import *
##
qubit1_spectro = loadtxt("spectroqubit1.txt",skiprows = 1,delimiter = "\t")
qubit2_spectro = loadtxt("spectroqubit2.txt",skiprows = 1,delimiter = "\t")
qubit1_spectro_simulation = loadtxt("spectroqubit1_fit.txt")
qubit2_spectro_simulation = loadtxt("spectroqubit2_fit.txt")
##
import matplotlib.gridspec as gridspec
gs = gridspec.GridSpec(1, 3,width_ratios = [3,3,1])
figure(2)
clf()
subplot(gs[0])
x0 = -1.619
dx = 30.819
xlabel("flux [$\Phi_0$]")
ylabel("frequency [GHz]")
plot((qubit1_spectro_simulation[:,0]-x0)/dx,qubit1_spectro_simulation[:,1],'r')
plot((qubit1_spectro_simulation[:,0]-x0)/dx,qubit1_spectro_simulation[:,2],'b')
plot((qubit2_spectro_simulation[:,0]-x0)/dx,qubit2_spectro_simulation[:,1],'r')
plot((qubit2_spectro_simulation[:,0]-x0)/dx,qubit2_spectro_simulation[:,2],'b')
plot((qubit1_spectro[:,0]-x0)/dx,qubit1_spectro[:,1],'+',color = 'black')
plot((qubit1_spectro[:,0]-x0)/dx,qubit1_spectro[:,2],'*',color = 'black')
plot((qubit2_spectro[:,0]-x0)/dx,qubit2_spectro[:,1],'+',color = 'black')
plot((qubit2_spectro[:,0]-x0)/dx,qubit2_spectro[:,2],'*',color = 'black')
axhline(6.84,color='black',ls='dotted')
axhline(6.70,color='black',ls='dashed')
ylim(4.0,8.7)
xlim(-0.05,0.75)
subplot(gs[1])
#anticrossing data from 2011/04/22
imshow(transpose(gv.m2),aspect = 'auto',origin = 'lower',interpolation = 'nearest',extent = (gv.survey["flux"][0],gv.survey["flux"][-1],gv.survey.children()[0]["f"][0],gv.survey.children()[0]["f"][-1]))
xlim(1.26,1.29)
ylim(5.1,5.15)
xticks(arange(1.265,1.285,0.005))
axvline(1.275,color='red',ls='dashed',lw=2)
#ylabel("frequency [GHz]")
xlabel("flux [a.u.]")

plot(gv.vs,gv.ees[:,2]-gv.ees[:,0],color = 'red',lw = 2,ls = 'dashed')
plot(gv.vs,gv.ees[:,1]-gv.ees[:,0],color = 'red',lw = 2,ls = 'dashed')
subplot(gs[2])
plot(gv.surveyCurve["p1x"],gv.surveyCurve["f"])
ylim(5.1,5.15)
xticks([0.1,0.2])
show()