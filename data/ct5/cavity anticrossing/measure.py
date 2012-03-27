from helpers.instrumentsmanager import Manager
manager = Manager()
vna1 = manager.instrumentCopy("vna","vna_1",kwargs = {'visaAddress' : 'GPIB0::15'})
vna2 = manager.instrumentCopy("vna","vna_2",kwargs = {'visaAddress' : 'GPIB0::16'})
coil = manager.instrumentCopy("yokogawa","coil",kwargs = {'name': 'Transmon Coil','visaAddress' : 'GPIB0::2'})
vna1 = manager.reloadInstrument("vna_1")
vna2 = manager.reloadInstrument("vna_2")
coil = manager.reloadInstrument("coil")
import math
import time
def setCoilVoltage(voltage,step = 0.01,timeout = 0.1):
	cv = coil.voltage()
	while math.fabs(cv-voltage)>1e-4:
		time.sleep(timeout)
		if cv > voltage:
			if cv - voltage > step:
				cv = coil.setVoltage(cv - step)
			else:
				cv = coil.setVoltage(voltage)
		if cv < voltage:
			if voltage - cv > step:
				cv = coil.setVoltage(cv + step)
			else:	
				cv = coil.setVoltage(voltage)
print "Done"

def saveTrace(filename,trace):
	values = zeros((len(trace[0]),3))
	values[:,0] = trace[0]
	values[:,1] = trace[1]
	values[:,2] = trace[2]
	savetxt(filename,values)		
##
for instrument in manager.instruments():
	print instrument
##
print coil.voltage()
setCoilVoltage(-5.5)
##
r = arange(-3.5,-1.0,0.01)
print r
for x in r:
	print "Setting Vcoil = %g " % x
	setCoilVoltage(x)
	try:
		print "Waiting for VNA1..."
		vna2.triggerReset()
		vna1.waitFullSweep()
		print "Getting trace 1..."
		trace1 = vna1.getTrace()
		saveTrace("cavity-1-vcoil=%g.txt" % x,trace1)
		print "Getting trace 2..."
		trace2 = vna2.getTrace()
		saveTrace("cavity-2-vcoil=%g.txt" % x,trace2)
	except SystemExit:
		print "Exiting..."
		exit(0)
	except:
		print "An unkown error occured. Continuing anyway..."
		print sys.exc_info()
##
setCoilVoltage(3.0)
##Measure the anticrossing of one of the qubits...
def measureAnticrossing(points,vna,basename):
	traces = []
	for point in points:
		print point
		setCoilVoltage(point)
		print "Getting trace..."
		vna.waitFullSweep()
		trace = vna.getTrace()
		traces.append(trace)
		saveTrace(basename+"%g-2.txt" % coil.voltage(),trace)
		print "Done"
##
measureAnticrossing(arange(-3.39,-2.0,0.01),vna1,"cavity-1-vcoil=")
measureAnticrossing(arange(-2.5,-1.0,0.01),vna2,"cavity-2-vcoil=")
##
cla()
figure(10)
plots = []
colors = ['red','green','blue','yellow','magenta']
for trace in traces:
	color = colors.pop()
	plots.append(trace[0])
	plots.append(trace[2])
	scatter(trace[0],trace[2],c = color)
##
m = genfromtxt("cavity-1-m20db.txt")
cla()
plot(m[:,0],m[:,2],traces[0][0],traces[0][2],traces[1][0],traces[1][2],traces[2][0],traces[2][2],traces[3][0],traces[3][2],traces[4][0],traces[4][2])
legend(("-20 dB","-17 dB","-14 dB","-23 dB","-26 dB"))