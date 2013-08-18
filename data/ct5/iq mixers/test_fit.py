state = instrumentManager.saveState("teststate")
print state
##
instrumentManager.restoreState(state)
##
afg1.saveState("teststate")
afg1.turnOff()
##
print params
##
qubit1.loadFluxWaveform([12000,12000,12000]*1000)
qubit2.loadFluxWaveform([12000,12000,12000]*100)
##
qubit2.loadRabiPulse()
qubit1.setReadoutDelay(2000)
##
afg1.writeWaveform('USER1',[0]*201)
##
afg2.setWaveform("USER1")
##
jba1.setReadoutPulse()
jba2.setReadoutPulse()
##
print xxx
##
qubit1.setDriveFrequency(5.6)
##
acqiris.bifurcationMap()
print acqiris.Psw()
##
qubit2.initQubit()
##
register["readoutDelay"] = 600
##
qubit1.loadRabiPulse(0)
acqiris.bifurcationMap()
print acqiris.Psw()["p1x"]

##Rabi init

##Rabi measurement

##Spectro init

##Spectro measurement

##T1 init

##T1 measurement

##
print instrumentManager.parameters()
##
print register["readoutDelay"]
##
data= Datacube()
data.savetxt("test")
##
instrumentManager.reloadInstrument("qubit2")
figure("pulses")
cla()
for i in [0,1,3,6,12,24,48,100]:
	pulse = qubit2.gaussianPulse(length = i,flank = 3)
	print sum(pulse+1)/float(i)
	plot(pulse)
##
qubit2.setDriveFrequency(5.55)
qubit2.loadRabiPulse(4,gaussian = True)
##
import random
instrumentManager.reloadInstrument("jba2")
while True:
	level = random.random()
	print "Going to %g" % level
	print "Arrived at %g in %d steps." % (jba2.adjustSwitchingLevel(level,precision = 0.01,verbose = True))
##
jba2.calibrate()
##
data = Datacube("S curve")
dataManager.addDatacube(data)
cnt = 0
for i in arange(0.7,1.4,0.001):	
	qubit2_att.setVoltage(i)
	acqiris.bifurcationMap()
	p = acqiris.Psw()
	data.set(att  = i, psw = p["px1"])
	data.commit()
	cnt+= 1
##
figure("attenuation")
clf()
plot(data.column("att"),data.column("psw"))
