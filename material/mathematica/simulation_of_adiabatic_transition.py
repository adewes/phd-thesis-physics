##Imports...
import sys
from quantum.qulib import *
from quantum.plotting import *
from numpy.linalg import norm
from pyview.helpers.datamanager import DataManager
from pyview.lib.datacube import *
from pyview.gui.datamanager import startDataManager
import matplotlib

matplotlib.use("module://pyview.gui.mpl.backend_static")
from matplotlib.pylab import *

dataManager = DataManager()
startDataManager()


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
		print "t = %g" % tt
		rhos[i] = rho_t
		i+=1
	return rhos

##Simulate a quantum process

tomography = Datacube("simulation of quantum process tomography")
densityMatrices = Datacube("density matrices",dtype =complex128)
tomography.addChild(densityMatrices,name = "density matrices")
dataManager.addDatacube(tomography)

#We store the parameters of the simulation in the datacube

g = 0.1

times = arange(0,40,0.1)

Delta = 0*math.pi*2.0
Delta1 = 0
Delta2 = 0

measurements = ["xx","xy","xz","yx","yy","yz","zx","zy","zz","xi","yi","zi","ix","iy","iz","ii"]
matrixMap = {"x":sigmax,"y":sigmay,"z":sigmaz,"i":idatom}

states = [(tensor(es,gs)-tensor(gs,es))/sqrt(2.0)]

print states

idtot = tensor(idatom,idatom)
drive1 = tensor(sigmax,idatom)
sm1 = tensor(sigmam,idatom)
sm2 = tensor(idatom,sigmam)
sp1 = tensor(sigmap,idatom)
sp2 = tensor(idatom,sigmap)
sz1 = tensor(sigmaz,idatom)
sz2 = tensor(idatom,sigmaz)

gamma1 = 0*1.0/560.
gamma2 = 0*1.0/530.
gammaphi1 = 0*1.0/1600.
gammaphi2 = 0*1.0/1400.

C1T1 = sqrt(gamma1)*sm1
C2T1 = sqrt(gamma2)*sm2
C1Phi = sqrt(gammaphi1/2.0)*sz1
C2Phi = sqrt(gammaphi2/2.0)*sz2

C1T1dC1T1 = adjoint(C1T1)*C1T1
C2T1dC2T1 = adjoint(C2T1)*C2T1
C1PhidC1Phi = adjoint(C1Phi)*C1Phi
C2PhidC2Phi = adjoint(C2Phi)*C2Phi

L1 = spre(C1T1)*spost(adjoint(C1T1))-0.5*spre(C1T1dC1T1)-0.5*spost(C1T1dC1T1)
L2 = spre(C2T1)*spost(adjoint(C2T1))-0.5*spre(C2T1dC2T1)-0.5*spost(C2T1dC2T1)
L3 = spre(C1Phi)*spost(adjoint(C1Phi))-0.5*spre(C1PhidC1Phi)-0.5*spost(C1PhidC1Phi)
L4 = spre(C2Phi)*spost(adjoint(C2Phi))-0.5*spre(C2PhidC2Phi)-0.5*spost(C2PhidC2Phi)
L = L1+L2+L3+L4

tomography.parameters()["gamma1"] = gamma1
tomography.parameters()["gamma2"] = gamma2
tomography.parameters()["gammaphi1"] = gammaphi1
tomography.parameters()["gammaphi2"] = gammaphi2
tomography.parameters()["g"] = g

def Lswap(t):

	"""
	This function returns the Lindblad operator for the Grover search algorithm
	"""
	if t > 10 and t < 20:
		delta = 100*g
	else:
		delta = 0
	exp_factor = delta+Delta2-Delta1
	H = matrix([[0,0,0,0],[0,Delta2,0,0],[0,0,Delta1,0],[0,0,0,Delta1+Delta2]])+g/2.0*sp1*sm2*exp(1j*exp_factor*t)+g/2.0*sm1*sp2*exp(-1j*exp_factor*t)
	LH = -1.j*(spre(H)-spost(H))
	return LH+L

for i in range(0,len(states)):
	cube = Datacube("state no %d" % i)
	tomography.addChild(cube,i = i)
	rho = vectorizeRho(adjoint(states[i])*states[i])
	cube.parameters()["defaultPlot"]=[["t","zzp00"],["t","zzp01"],["t","zzp10"],["t","zzp11"]]
	rhos = integrate(rho,Lswap,times,dt = 0.01)
	for j in range(0,len(times)):
		rho = devectorizeRho(rhos[j])
		cube.set(t = times[j])
		cube.set(zzp00 = rho[0,0],zzp10 = rho[1,1],zzp01 = rho[2,2],zzp11 = rho[3,3])
		for measurement in measurements:
			cube.set(**{measurement:trace(rho*tensor(matrixMap[measurement[0]],matrixMap[measurement[1]]))})
		cube.commit()
		cube.set(phase = angle(rho[1,2]))
	for a in range(0,4):
		for b in range(0,4):
			densityMatrices.setAt(i,**{str(a)+str(b):devectorizeRho(rhos[-1])[a,b]})
	figure("swap")
	subplot(121)
	cla()
	plotDensityMatricesContour([devectorizeRho(rhos[0])],annotate = True)
	subplot(122)
	cla()
	plotDensityMatricesContour([devectorizeRho(rhos[1])],annotate = True)
	show()

print "Press [Enter] to continue..."
sys.stdin.readline()
