import matplotlib
matplotlib.use('module://pyview.gui.mpl.backend_static')
from matplotlib.pyplot import *
from numpy import *
from pyview.lib.datacube import *

survey = Datacube()
survey.loadtxt("Spectroscopy Survey - qubit1-9")

figure(10)
clf()
m1 = zeros((len(survey),len(survey.children()[0])))
m2 = zeros((len(survey),len(survey.children()[0])))
for i in range(0,len(survey)):
	m1[i,:] = survey.children()[i]["p1x"]
	m2[i,:] = survey.children()[i]["px1"]

subplot(121)	
imshow(transpose(m1),aspect = 'auto',origin = 'lower',interpolation = 'nearest',extent = (survey["flux"][0],survey["flux"][-1],survey.children()[0]["f"][0],survey.children()[0]["f"][-1]))

xlim(1.26,1.29)
ylim(5.1,5.15)
title("Anticrossing spectroscopy - p1x")
xlabel("fluxline I voltage [V]")
ylabel("drive frequency [GHz]")

subplot(122)	
imshow(transpose(m2),aspect = 'auto',origin = 'lower',interpolation = 'nearest',extent = (survey["flux"][0],survey["flux"][-1],survey.children()[0]["f"][0],survey.children()[0]["f"][-1]))
xlim(1.26,1.29)
ylim(5.1,5.15)
title("Anticrossing spectroscopy - px1")
xlabel("fluxline I voltage [V]")
ylabel("drive frequency [GHz]")
figtext(0.02,0.02,survey.filename()[:-4])
show()

import sys
sys.stdin.readline()