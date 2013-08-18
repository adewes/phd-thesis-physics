##Measure the T1 of a qubit at different values of flux.
qubit = qubit2
voltages = arange(-1.8,-1.6,0.025)
freqs = arange(5.9,6.3,0.004)
afg = afg2
jba = jba2
variable = "px1"
name = "Qubit 2"
##
qubit = qubit1
voltages = arange(-1.5,-1.2,0.0025)
freqs = arange(6.0,6.2,0.002)
afg = afg1
jba = jba1
variable = "p1x"
name = "Qubit 1"
##
reload(sys.modules["macros.qubit_functions"])
from macros.qubit_functions import *

survey = Datacube("T1 survey - %s" % name)
qubit.initQubit()
survey.setParameters(instrumentManager.parameters())
dataManager.addDatacube(survey)
try:
	automaticT1(qubit,voltages,freqs,jba,variable,datacube = survey,cavity = 6.8,voltageRead = afg.offset,voltageWrite = afg.setOffset)
finally:
	survey.savetxt()
##
try:
	reload(sys.modules["macros.qubit_functions"])
	from macros.qubit_functions import *
	scurve = Datacube("S Curves")
	dataManager.addDatacube(scurve)
	measureSCurves(qubit1,jba1,cube = scurve)
finally:
	scurve.savetxt()
##
figure("swap")
cla()
plot(swap.column("duration"),swap.column("p00"))
plot(swap.column("duration"),swap.column("p01"))
plot(swap.column("duration"),swap.column("p10"))
plot(swap.column("duration"),swap.column("p11"))
xlabel("interaction time [ns]")
ylabel("switching probability")
legend((r"p$\left(\|00\rangle\right)$",r"p$\left(\|01\rangle\right)$",r"p$\left(\|10\rangle\right)$",r"p$\left(\|11\rangle\right)$"))
title("Quantul Swap between Qubit 1 & Qubit 2")