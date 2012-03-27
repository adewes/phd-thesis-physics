instrumentManager.reloadInstrument("qubit1")
data = Datacube()
data.loadtxt("response function - whole line - normalized")
qubit1.setFluxlineResponse(data)
##
waveform = zeros(100)-1.0
waveform[50:70] = 1.0
import time
start = time.time()
output  = qubit1.loadFluxlineWaveform(waveform)
print time.time()-start
figure("correction")
cla()
plot(output)
