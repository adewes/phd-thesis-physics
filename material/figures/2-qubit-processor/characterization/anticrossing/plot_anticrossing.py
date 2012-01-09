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

m1 = zeros((len(datacube.children()[0]),len(datacube)))
m2 = zeros((len(datacube.children()[0]),len(datacube)))

for i,child in enumerate(datacube.children()):
	m1[:,i] = child["p1x"] 
	m2[:,i] = child["px1"] 

##

print "Generating figure \"%s\"" % titleString

f = figure(1)
f.set_size_inches((params["figureStandardWidth"],params["figureStandardHeight"]))
clf()

subplot(121)
imshow(m1,origin = 'upper',aspect = 'auto',interpolation = 'nearest',extent = (datacube["flux"][0],datacube["flux"][-1],datacube.children()[0]["f"][-1],datacube.children()[0]["f"][0]))

xlim(1.27,1.28)
ylim(5.1,5.15)
title("Qubit 1 - Switching Probability")

subplot(122)
imshow(m2,origin = 'upper',aspect = 'auto',interpolation = 'nearest',extent = (datacube["flux"][0],datacube["flux"][-1],datacube.children()[0]["f"][-1],datacube.children()[0]["f"][0]))

xlim(1.27,1.28)
ylim(5.1,5.15)
title("Qubit 2 - Switching Probability")

for outputFormat in params["figureOutputFormats"]:
    filename = "%s.%s" % (outputFilename,outputFormat)
    print "Saving figure as \"%s\"" % filename
    savefig(filename)

if "-i" in sys.argv:
    show()
    print "[press any key to exit]"
    sys.stdin.readline()

print "Done..." 