##We create different qubit states and measure the switching probability of the JBA after applying I,Q pulses of different lengths (like in Steffen, PRL 97 050502 2006 http://www.physics.ucsb.edu/~martinisgroup/papers/Steffen2006.pdf)

reload(sys.modules["instruments.qubit"])
from instruments.qubit import *

waveform = zeros(6000)
waveform[1:-1] = 0.8

data = Datacube("IQ tomography")
data.setParameters(instrumentManager.parameters())
dataManager.addDatacube(data)
delay = 3000

margin1 = 3
margin2 = 3

f_sb = -0.12

#State preparation...

preparation = PulseSequence()

qubit2.setDriveFrequency(qubit2.parameters()["frequencies.f01"]+f_sb)
qubit2.setDriveAmplitude(I = qubit2.parameters()["pulses.xy.drive_amplitude"],Q = qubit2.parameters()["pulses.xy.drive_amplitude"])

#State |0> (we do nothing :)

#State |1>

#preparation.addPulse(qubit2.generateRabiPulse(phase = math.pi,f_sb = f_sb,delay = delay,angle = 0))

#State |0>+|1>
#preparation.addPulse(qubit2.generateRabiPulse(phase = math.pi/2.0,f_sb = f_sb,delay = delay,angle = 0))

#State |0>+i*|1>
preparation.addPulse(qubit2.generateRabiPulse(angle = math.pi/2.0,phase = math.pi/2.0,f_sb = f_sb,delay = delay))

delta_f_12 = -qubit2.parameters()["frequencies.f02"]+2*qubit2.parameters()["frequencies.f01"]

Ivalues = arange(-1,1.1,0.05)
Qvalues = arange(-1,1.1,0.05)

matrix= zeros((len(Ivalues),len(Qvalues)))

#...and measurement:

figure("matrix")

clf()
cla()

imshow(matrix)

x = 0	
for I in Ivalues:
	y = 0
	for Q in Qvalues:
		drive = PulseSequence()

		drive.addPulse(preparation.getWaveform())

		pulse = qubit2.generateRabiPulse(length = 30,f_sb = f_sb,delay = len(drive),angle = 0)*0.5

		pulse *=I+1j*Q

		drive.addPulse(pulse)

		qubit2.loadWaveform(drive.getWaveform(),len(drive)+1)
	
		acqiris.bifurcationMap(ntimes  = 50)
		
		psw = acqiris.Psw()

		data.set(**psw)
		data.set(I = I,Q = Q)
		data.commit()
		data.savetxt()
		
		matrix[x,y] = psw["px1"]
	
		y+=1

	imshow(matrix)
	x+=1
##
clf()
imshow(matrix,extent = (-1,1,-1,1))
xlabel("I quadrature amplitude")
ylabel("Q quadrature amplitude")
##
figure("test")
cla()
f = lambda x: (-cos(x)*(1.0-0.5*cos(x/2))/2+1)
xs = arange(0,100,0.1)
plot(xs,f(xs))
##
figure("pulse")
subplot(211)
cla()
plot(real(qubit2.generateRabiPulse(length = 100,angle = 0,f_sb = 0.1)))
plot(real(qubit2.generateRabiPulse(length = 100,angle = math.pi/2,f_sb = 0.1)))
subplot(212)
cla()
plot(imag(qubit2.generateRabiPulse(length = 100,angle = 0,f_sb = 0.1)))
plot(imag(qubit2.generateRabiPulse(length = 100,angle = math.pi/2,f_sb = 0.1)))