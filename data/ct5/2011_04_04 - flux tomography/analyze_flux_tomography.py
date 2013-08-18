from numpy import *
from scipy.linalg import eigh,cholesky
import matplotlib
matplotlib.use('module://pyview.gui.mpl.backend_static')
from matplotlib.pyplot import *
import sys

import numpy

import quantum.plotting
reload(sys.modules["quantum.plotting"])
from quantum.plotting import plotDensityMatricesContour

import quantum.qulib
reload(sys.modules["quantum.qulib"])
from quantum.qulib import *
##
figure(33)
clf()
subplot(311)
signal = zeros(2000)
ts = linspace(0,len(signal),len(signal))
signal[1000:] = 1.0

from scipy.interpolate import interp1d

ts_measured = linspace(gv.data["t"][0],gv.data["t"][-1],gv.data["t"][-1]-gv.data["t"][0])

dataInterpolation = interp1d(gv.data["t"],gv.data["flux"])
signalInterpolation = interp1d(ts,signal)

ts_diff = ts_measured[1:]

measuredData = -dataInterpolation(ts_measured)
measuredData -= measuredData[0]
measuredData/= max(measuredData)-min(measuredData)
signalData = signalInterpolation(ts_measured)

measuredDiffs = measuredData[1:]-measuredData[:-1]
signalDiffs = signalData[1:]-signalData[:-1]

from qubit_setup.instruments.qubit import gaussianFilter

response = gaussianFilter(linspace(0,1.0,len(numpy.fft.rfft(signalData))),cutoff = 0.4)
responseDiffs = gaussianFilter(linspace(0,1.0,len(numpy.fft.rfft(signalDiffs))),cutoff = 0.4)

signalfft = numpy.fft.rfft(signalData)

dsignalfft = numpy.fft.rfft(signalDiffs)
dmeasuredfft = numpy.fft.rfft(measuredDiffs)

freqs = linspace(0,0.5,len(dmeasuredfft))
responseFunction = interp1d(freqs,dmeasuredfft/dmeasuredfft[0]/dsignalfft)

plot(ts_measured-950,measuredData)
plot(ts_measured-950,signalData)
plot(ts_measured-950,numpy.fft.irfft(signalfft/responseFunction(linspace(0,0.5,len(signalfft)))*gaussianFilter(linspace(0,0.5,len(signalfft)),cutoff = 0.12),len(ts_measured)))

xlim(0,100)

ylabel("signal")

subplot(312)

plot(ts_diff,measuredDiffs)
plot(ts_diff,signalDiffs)

ylabel("signal derivative")

subplot(313)

plot(freqs,abs(dmeasuredfft/dmeasuredfft[0]))
plot(freqs,imag(responseFunction(freqs)))
plot(freqs,abs(dsignalfft))

ylabel("FFT")
xlabel("frequency [GHz]")

show()

##Write the response function to a file...

response = Datacube("response function",dtype = complex128)
response.setColumn("frequency",freqs)
response.setColumn("response",responseFunction(freqs))
response.savetxt()

##

register["calibration.fluxline.qubit1"] = response.filename()