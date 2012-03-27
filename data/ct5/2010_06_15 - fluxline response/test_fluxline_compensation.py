import numpy.fft
import scipy
import scipy.interpolate


def filter(x,cutoff = 0.5):
	return exp(-pow(scipy.fabs(real(x))/cutoff,2.0) )

data = Datacube()
data.loadtxt("response function - whole line-2-1")
responseFunctionWaveformSample = data.column("response_waveform_sample")

offset = responseFunctionWaveformSample[0]
data.table()[0,:] = 1.0
data.column('frequency')[0] = 0
print data.table()
print absolute(offset)
responseFunctionWaveformSample[0] = complex(1.0,offset.imag)

freqs = data.column("frequency")

waveformLength = (len(freqs)-1)*2*6

##

testWaveform = zeros(waveformLength)
testWaveform[waveformLength/2-100:waveformLength/2+100] = 1.0
testWaveformFFT = numpy.fft.rfft(testWaveform)
testWaveformSampleFFT = numpy.fft.rfft(testWaveform)

response = scipy.interpolate.interp1d(freqs,responseFunctionWaveformSample)
responseADC = scipy.interpolate.interp1d(freqs, data.column("response_adc"))
responseSample = scipy.interpolate.interp1d(freqs, data.column("response_input_sample"))

interpolatedFreqs = linspace(0,2.0,len(testWaveformFFT))

responseInterpolation = response(interpolatedFreqs)
responseADCInterpolation = responseADC(interpolatedFreqs)
responseSampleInterpolation = responseSample(interpolatedFreqs)
filterValues = filter(interpolatedFreqs,cutoff = 0.45)
figure("response function interpolation")
cla()
plot(interpolatedFreqs,real(response(interpolatedFreqs)),freqs,real(responseFunctionWaveformSample),'ro')
plot(interpolatedFreqs,imag(response(interpolatedFreqs)),freqs,imag(responseFunctionWaveformSample),'bo')
##
import time
start = time.time()

testWaveformFFT/=responseInterpolation/filterValues
testWaveformSampleFFT = testWaveformFFT*responseInterpolation
	
correctedWaveform = numpy.fft.irfft(testWaveformFFT)
correctedWaveformSample = numpy.fft.irfft(testWaveformSampleFFT)
testWaveform = (testWaveform-min(testWaveform))/(max(testWaveform)-min(testWaveform))
print "needed %g s" % (time.time()-start)
##
figure("correction test")
clf()
plot(testWaveform)
plot(correctedWaveform)
plot(correctedWaveformSample)
plot(numpy.fft.irfft(numpy.fft.rfft(correctedWaveformSample)*responseADCInterpolation*responseSampleInterpolation))

##Write the corrected waveform to the AFG and measure the returning signal:
acqiris2 = instrumentManager.initInstrument("rip://192.168.0.19:8000/acqiris2","acqiris")
target = correctedWaveform
afg1.writeWaveform("USER1",(target-min(target))/(max(target)-min(target))*(2<<13)-1)
afg1.setWaveform("USER1")
waveformLength = len(correctedWaveform)
acqiris2.ConfigureV2(**{'numberOfPoints':waveformLength,'sampleInterval':0.5e-9,'delayTime':0,'numberOfSegments':1,'triggerSlope':2})
afg1.setPeriod(waveformLength/2.0)
afg1.turnOff()
acqiris2.bifurcationMap(ntimes = 100000)
noise = acqiris2.averages()[0]
afg1.turnOn()
acqiris2.bifurcationMap(ntimes = 100000)
output = acqiris2.averages()[0]-noise
##Plot the results:

figure("correction test")
clf()
title("response function correction - test measurement")
signalAtSample = numpy.fft.irfft(numpy.fft.rfft(output)/responseSampleInterpolation/responseADCInterpolation)
output = (output-min(output))/(max(output)-min(output)) 
times = linspace(0,len(output)*0.5,len(output))
plot(times,output)
plot(times,(target-min(target))/(max(target)-min(target)))
plot(times,testWaveform)
plot(times,numpy.fft.irfft(numpy.fft.rfft(testWaveform)))
plot(times,signalAtSample)
xlim(0,times[-1])
ylim(-0.1,1.1)
xlabel('time [ns]')
ylabel('voltage [arb.]')
legend(["signal at output","signal provided at input","desired waveform at sample","calculated signal at sample"])