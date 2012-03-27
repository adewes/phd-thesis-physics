import matplotlib
matplotlib.use('module://pyview.gui.mpl.backend')
from matplotlib.pyplot import *
from numpy import *
figure(10)
clf()
m1 = zeros((len(gv.survey),len(gv.survey.children()[0])))
m2 = zeros((len(gv.survey),len(gv.survey.children()[0])))
for i in range(0,len(gv.survey)):
	m1[i,:] = gv.survey.children()[i]["p1x"]
	m2[i,:] = gv.survey.children()[i]["px1"]
gv.m2 = m2
subplot(121)	
imshow(transpose(m1),aspect = 'auto',origin = 'lower',interpolation = 'nearest',extent = (gv.survey["flux"][0],gv.survey["flux"][-1],gv.survey.children()[0]["f"][0],gv.survey.children()[0]["f"][-1]))

xlim(1.26,1.29)
ylim(5.1,5.15)
title("Anticrossing spectroscopy - p1x")
xlabel("fluxline I voltage [V]")
ylabel("drive frequency [GHz]")

subplot(122)	
imshow(transpose(m2),aspect = 'auto',origin = 'lower',interpolation = 'nearest',extent = (gv.survey["flux"][0],gv.survey["flux"][-1],gv.survey.children()[0]["f"][0],gv.survey.children()[0]["f"][-1]))
xlim(1.26,1.29)
ylim(5.1,5.15)
title("Anticrossing spectroscopy - px1")
xlabel("fluxline I voltage [V]")
ylabel("drive frequency [GHz]")
figtext(0.02,0.02,gv.survey.filename()[:-4])
show()
