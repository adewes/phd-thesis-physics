import matplotlib
matplotlib.use('module://pyview.gui.mpl.backend')

from numpy import *
from matplotlib.pyplot import *	

import csv

##
from pyview.lib.datacube import Datacube
from pyview.helpers.datamanager import DataManager
import re
filename = "qubit_chip_sonnet_model.csv"
dataManager = DataManager()
file = open(filename,"rb")
content = file.read()
file.close()
lines = content.split("\n")
curves = Datacube("curves")
dataManager.clear()
dataManager.addDatacube(curves)
i = 0
curve = None
while i < len(lines):
	elements = lines[i].split(",")
	if re.search("l1=(\d+\.\d+)",lines[i],re.I):
		if curve != None and len(curve) == 0:
			curves.removeChild(curve)
		print lines[i]
		lq = float(re.search("l1=(\d+\.\d+)",lines[i],re.I).group(1))
		print lq
		i+=2
		if i >= len(lines):	
			break
		curve = Datacube("l1 = %g nH" % lq)
		curves.addChild(curve,lq = lq)
		curve.parameters()["defaultPlot"] = [("freq","mag")]
	elif len(elements) == 2:
		(freq,mag) = map(lambda x:float(x),lines[i].split(","))
		curve.set(freq = freq,mag = mag)
		curve.commit()
	i+=1	
curves.savetxt("sonnet_model")
##
import os
from numpy import *
m = zeros((len(curves.children()[0]),len(curves.children())))
i = 0
for child in curves.children():
	print mean(child["mag"]),max(child["mag"])
	m[:,i] = child["mag"]
	i+=1
m = m [::-1]
figure(10)
clf()
hsv()
imshow(m,aspect = 'auto',interpolation = 'bilinear',extent = (curves.attributesOfChild(curves.children()[0])["lq"],curves.attributesOfChild(curves.children()[-1])["lq"],child["freq"][0],child["freq"][-1]))
ticklabel_format(style = 'plain',axis = 'y',useOffset = False)
#figtext(0.1,0.95,os.getcwd()+"/"+filename,size = 7)
#ylim(11,12)
#xlim(2,2.3)
xlabel("$L_{qb}$ [nH]")
ylabel("frequency [GHz]")
show()
import sys
sys.stdin.readline()
