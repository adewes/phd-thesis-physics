waveform = zeros(7000)
linform = linspace(0,1,1000)
sqform = sqrt(linform)
waveform[0:1000] = waveform[0] + (0.8-waveform[0])*sqform 
waveform[1000:qubit2.readoutDelay()-10] = 0.8
qubit2.parameters()["flux.readout"] = 0.75
waveform[qubit2.readoutDelay()-10:len(waveform)] = qubit2.parameters()["flux.readout"]
figure("fluxline")
cla()
plot(waveform)
qubit2.loadFluxlineWaveform(waveform)