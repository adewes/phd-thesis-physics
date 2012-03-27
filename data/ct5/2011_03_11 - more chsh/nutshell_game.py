from qulib import *

state0 = transpose(tensor(gs,gs))

rho0 = state0*adjoint(state0)

rot1 = tensor(roty(math.pi/2.0),roty(math.pi/2.0))

state1 = rot1*state0


rho1 = rot1*rho0*adjoint(rot1)

swap = lambda phi: matrix([[1,0,0,0],[0,cos(phi),1j*sin(phi),0],[0,1j*sin(phi),cos(phi),0],[0,0,0,1]],dtype = complex128)

rho2 = swap(math.pi/2.0)*rho1*adjoint(swap(math.pi/2.))

state2 = swap(math.pi/2.0)*state1

rot2 = tensor(rotz(math.pi/2.0),rotz(-math.pi/2.0))

rho3 = rot2*rho2*adjoint(rot2)
state3 = rot2*state2

print state1
print state2
print state3
