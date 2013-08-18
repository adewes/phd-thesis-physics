##Imports...
import sys
from quantum.qulib import *
from quantum.plotting import *
import matplotlib
from scipy.optimize import fmin_powell
from numpy.linalg import norm
from pyview.helpers.datamanager import DataManager
from pyview.gui.datamanager import startDataManager
dataManager = DataManager() 
##Parameter definitions...
alpha = -2.0*math.pi*0.24
beta = -2.0*math.pi*0.24

gamma10_1 = 0*1.0/353.4
gamma10_2 = 0*1.0/368.7
gammaphi10_1 = 0*1.0/500.0
gammaphi10_2 = 0*1.0/650.0

##Some more definitions...

sm10 = matrix([[0,1,0],[0,0,0],[0,0,0]])
sp10 = matrix([[0,0,0],[1,0,0],[0,0,0]])
sm21 = matrix([[0,0,0],[0,0,1],[0,0,0]])
sp21 = matrix([[0,0,0],[0,0,0],[0,1,0]])
sm20 = matrix([[0,0,1],[0,0,0],[0,0,0]])
sp20 = matrix([[0,0,0],[0,0,0],[1,0,0]])

id3 = matrix([[1,0,0],[0,1,0],[0,0,1]])

sz10 = matrix([[1,0,0],[0,-1,0],[0,0,0]])
sz21 = matrix([[0,0,0],[0,1,0],[0,0,-1]])
sz20 = matrix([[1,0,0],[0,0,0],[0,0,-1]])

idtot = tensor(id3,id3)

sm10_1 = tensor(sm10,id3)
sm21_1 = tensor(sm21,id3)
sm20_1 = tensor(sm20,id3)

sm10_2 = tensor(id3,sm10)
sm21_2 = tensor(id3,sm21)
sm20_2 = tensor(id3,sm20)

sz10_1 = tensor(sz10,id3)
sz21_1 = tensor(sz21,id3)
sz20_1 = tensor(sz20,id3)

sz10_2 = tensor(id3,sz10)
sz21_2 = tensor(id3,sz21)
sz20_2 = tensor(id3,sz20)

CT10_1  = sqrt(gamma10_1)*sm10_1
CT10_2  = sqrt(gamma10_2)*sm10_2
CPhi10_1 = sqrt(gammaphi10_1/2.0)*sz10_1
CPhi10_2 = sqrt(gammaphi10_2/2.0)*sz10_2

P_CT10_1  = adjoint(CT10_1)*CT10_1
P_CT10_2  = adjoint(CT10_2)*CT10_2
P_CPhi10_1 = adjoint(CPhi10_1)*CPhi10_1
P_CPhi10_2 = adjoint(CPhi10_2)*CPhi10_2

L1 = spre(CT10_1)*spost(adjoint(CT10_1))-0.5*spre(P_CT10_1)-0.5*spost(P_CT10_1)
L2 = spre(CT10_2)*spost(adjoint(CT10_2))-0.5*spre(P_CT10_2)-0.5*spost(P_CT10_2)
L3 = spre(CPhi10_1)*spost(adjoint(CPhi10_1))-0.5*spre(P_CPhi10_1)-0.5*spost(P_CPhi10_1)
L4 = spre(CPhi10_2)*spost(adjoint(CPhi10_2))-0.5*spre(P_CPhi10_2)-0.5*spost(P_CPhi10_2)
L = L1+L2+L3+L4

##The simulation...


	
#dataManager.addDatacube(cube)

Delta10 = 0.0
Delta21 = Delta10-beta+alpha
g = 0.0082*2.0*math.pi/2.0

state = tensor(matrix([1,0,0]),matrix([1,0,0]))
state = state/norm(state)
rho = vectorizeRho(adjoint(state)*state)


coupling = lambda Delta10,g,t: matrix([
	[0,0,0,0,0,0,0,0,0],
	[0,0,0,g*exp(1j*Delta10*t),0,0,0,0,0],
	[0,0,0,0,sqrt(2)*g*exp(1j*(-beta+Delta10)*t),0,0,0,0],
	[0,g*exp(-1j*Delta10*t),0,0,0,0,0,0,0],
	[0,0,sqrt(2)*g*exp(-1j*(-beta+Delta10)*t),0,0,0,sqrt(2)*g*exp(1j*(alpha+Delta10)*t),0,0],
	[0,0,0,0,0,0,0,2.*g*exp(1j*(alpha+Delta10-beta)*t),0],
	[0,0,0,0,sqrt(2)*g*exp(-1j*(alpha+Delta10)*t),0,0,0,0],
	[0,0,0,0,0,2.*g*exp(-1j*(alpha+Delta10-beta)*t),0,0,0],
	[0,0,0,0,0,0,0,0,0]	
])

drive1 = lambda epsilon,t: tensor(matrix(
	[
		[0,conjugate(epsilon),0],
		[epsilon,0,sqrt(2.)*conjugate(epsilon)*exp(1j*t*alpha)],
		[0,sqrt(2.)*epsilon*exp(-1j*t*alpha),0]
	]),id3)

drive2 = lambda epsilon,t: tensor(id3,matrix(
	[
		[0,conjugate(epsilon),0],
		[epsilon,0,sqrt(2.)*conjugate(epsilon)*exp(1j*t*beta)],
		[0,sqrt(2.)*epsilon*exp(-1j*t*beta),0]
	])
)

stateLabels = ["00","10","20","01","11","21","02","12","22"]

def integrate(rho,L,ts,dt = 0.1):

	t = 0
	
	rhos = zeros((len(ts),rho.shape[0],rho.shape[1]),dtype = complex128)

	def rungeKuttaIntegrate(rho,L,t,dt):
		L2 = L(t+dt/2.)
		k1 = dt*L(t)*rho
		k2 = dt*L2*(rho+k1/2.)
		k3 = dt*L2*(rho+k2/2.)
		k4 = dt*L(t+dt)*(rho+k3/2.)
		return rho+1./6.*(k1+2.*k2+2.*k3+k4)

	def adaptiveIntegrate(rho,L,t,dt,epsilon = 0.001,epsilonTrace = 1e-7):
		rho1 = rho.copy()
		t_array = [t,t+dt]
		L_array = [L(t_array[0]),L(t_array[1])]
		while True:
#			print t_array
			rhon = rho.copy()
			for i in range(0,len(t_array)-1):
				rhon =rhon+L_array[i]*(t_array[i+1]-t_array[i])*rhon
			e1 = norm(rho1-rhon)
			e2 = abs(sum(rhon[range(0,len(rhon),int(sqrt(len(rhon))+1)),0])-1)
			if sqrt(abs(e2)) > epsilonTrace or e1 > epsilon:
				for t in range(1,len(t_array)):
					nt = t_array[t-1]+(t_array[t]-t_array[t-1])/2.
					t_array.insert(t,nt)
					L_array.insert(t,L(nt))
			else:
				break
			rho1 = rhon
#		print "Required %d steps" % len(t_array)
		return rhon

	i = 0
	
	ts = list(ts)
	
	integrationMethod = rungeKuttaIntegrate

	rho_t = rho.copy()

	while len(ts) > 0:
		tt = ts.pop(0)
		#print "t = %g " % tt
		dtt = dt
		while t < tt:
			if tt-t > dt:
				rho_t = integrationMethod(rho_t,L,t,dt)
				t+=dt
			else:
				rho_t = integrationMethod(rho_t,L,t,tt-t)
				t+=tt-t
		rhos[i] = rho_t
		i+=1
	return rhos

def L_drive(t,delta = 0):
	extra = drive1(0.2,t)
	g = 0./math.pi
	H = coupling(Delta10,g,t)+extra
	LH = -1.j*(spre(H)-spost(H))
	return LH+L

def gaussianPulse(t,t0,flank = 4):
	return exp(-0.5*pow((t-t0)/flank*3.0,2.0))

def rectanglePulse(t,t0,t1,flank = 3):
	if t >= t1:
		return max(0.,1.-(t-t1)/flank)
	elif t > t0-flank:
		return min(1,(t-t0+flank)/flank)
	else:
		return 0

t_gate_start = 15.
t_gate_end = t_gate_start+1.0/g/8.*2.*math.pi+1.0

print t_gate_end

def delta_qq_eff(t,delta_qq):
	return delta_qq*(1.0-rectanglePulse(t,t_gate_start,t_gate_end,flank = 2.0))

def epsilon_1(t,a,delta,phi):
	return gaussianPulse(t,8)*a*exp(-1.j*delta*t-1.j*phi)

def epsilon_2(t,a,delta,phi):
	return gaussianPulse(t,8)*a*exp(-1.j*delta*t-1.j*phi)

def L_swap(t,a1=0,delta1=0,phi1=0,a2=0,delta2=0,phi2=0,delta_qq=0):
#	g = 0.2/math.pi
	H = drive1(epsilon_1(t,a1,delta1,phi1),t)+drive2(epsilon_2(t,a2,delta2,phi2),t)
	H+=coupling(delta_qq_eff(t,delta_qq),g,t)
	LH = -1.j*(spre(H)-spost(H))
	return LH+L

def L_drive(t,a,delta,phi):
	H = drive1(gaussianPulse(t,8)*a*exp(-1.j*delta*t-1.j*phi),t)
	LH = -1.j*(spre(H)-spost(H))
	return LH+L

times = arange(0,int(t_gate_end)+4.0,0.1)
delta_qq = 2.*math.pi*0.15
points = 3

l=0

def generate_image(cube,element):
	im = zeros((len(cube.children()),len(cube.children()[0])))
	for i in range(0,len(cube.children())):
		im[i,:] = cube.children()[i][element]
	return im

cube = Datacube("master equation simulation - swap 01-10",dtype=complex128)
dataManager.addDatacube(cube)

cube.parameters()["defaultPlot"]=[["t","zzp00"],["t","zzp01"],["t","zzp10"],["t","zzp11"]]
cube.parameters()["simulation"] = {'alpha':alpha,'beta':beta,'g':g,'gamma10_1':gamma10_1,'gamma10_2':gamma10_2,'gammaphi10_1':gammaphi10_1,'gammaphi10_2':gammaphi10_2,'delta_qq':delta_qq}

def optimizeDrivePulse(targetRho):
	def optimization_function(params,targetRho):
		print params
		finalRho = devectorizeRho(integrate(rho,lambda t:L_drive(t,a = params[0],delta = params[1],phi = params[2]),ts = arange(0,14,0.1),dt = 0.01)[-1])
		tf = 1.-abs(trace(finalRho*targetRho))
		print tf
		return tf
	params0 = [0.2,0,0]
	return fmin_powell(optimization_function,params0,args = [targetRho])

targetState = tensor(matrix([1,1,0]),matrix([1,0,0]))
targetState = targetState/norm(targetState)
targetRho = adjoint(targetState)*targetState
#print optimizeDrivePulse(targetRho)
#print "Done optimizing."
#exit(0)

input_rho_index = list(times).index(t_gate_start)
output_rho_index = list(times).index(int(t_gate_end+3.0))

print input_rho_index
print output_rho_index

inputs = [(0,0),(1,0),(0.5,0),(0.5,1.)]
combinations = [(inputs[i],inputs[j]) for i in range(0,len(inputs)) for j in range(0,len(inputs))]
print combinations

startDataManager(False)

def sv(q1,q2):
	m1 = [0,0,0]
	m2 = [0,0,0]
	m1[q1]=1
	m2[q2]=1
	return tensor(matrix(m1),matrix(m2))

def proj(q1,q2):
	return adjoint(sv(q1,q2))*sv(q1,q2)

sqrt_iSWAP = proj(0,0)+proj(1,1)+proj(0,2)+proj(2,0)+proj(1,2)+proj(2,1)+proj(2,2)+1./sqrt(2)*(proj(0,1)+proj(1,0)-1j*(adjoint(sv(1,0))*sv(0,1)+adjoint(sv(0,1))*sv(1,0)))

for input_drive in combinations:
	(a1,delta1,phi1,a2,delta2,phi2) = (-0.501*input_drive[0][0],-0.192,math.pi/2.0*input_drive[0][1],-0.501*input_drive[1][0],-0.192,math.pi/2.0*input_drive[1][1])
	rhos = integrate(rho,lambda t,input_drive = input_drive:L_swap(t,a1=a1,delta1 = delta1,phi1 = phi1,a2=a2,delta2=delta2,phi2=phi2,delta_qq=delta_qq),times,dt = 0.01)

	subcube = Datacube("swap",dtype = complex128)
	cube.addChild(subcube,input_drive = input_drive)

	waveforms = Datacube("waveforms",dtype = complex128)
	subcube.addChild(waveforms)

	for t in times:
		waveforms.set(delta = delta_qq_eff(t,delta_qq),epsilon_1 = epsilon_1(t,a1,delta1,phi1),epsilon_2 = epsilon_2(t,a2,delta2,phi2), t = t)
		waveforms.commit()

	for i in range(0,len(rhos)):
		subcube.set(t = times[i])
		rho_matrix = devectorizeRho(rhos[i])
		for j in range(0,len(rho_matrix)):
			for k in range(0,len(rho_matrix)):
				subcube.set(**{stateLabels[j]+stateLabels[k]:rho_matrix[j,k]})
		subcube.commit()
	l+=1

	input_rho = matrix(devectorizeRho(rhos[input_rho_index]))
	output_rho = matrix(devectorizeRho(rhos[output_rho_index]))
	output_rho_ideal = sqrt_iSWAP*input_rho*adjoint(sqrt_iSWAP)

	fidelity = stateFidelity(output_rho_ideal,output_rho)

	print "Fidelity: %g" % fidelity
	
	cube.set(fidelity = fidelity)

	clf()
	plotDensityMatricesContour([output_rho,output_rho_ideal],annotate = False)
	show()
	

	for density_matrix in [input_rho,output_rho,output_rho_ideal]:			
		for i in range(0,len(density_matrix)):
			for j in range(0,len(density_matrix)):
				cube.set(**{str(i)+str(j):density_matrix[i,j]})
		cube.commit()


m1010 = generate_image(cube,'1010')
m0101 = generate_image(cube,'0101')
m1111 = generate_image(cube,'1111')
m2020 = generate_image(cube,'2020')
m0202 = generate_image(cube,'0202')
cube.savetxt("swap simulation")

import sys
sys.stdin.readline()