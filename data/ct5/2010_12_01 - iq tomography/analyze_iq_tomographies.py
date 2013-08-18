from pyview.lib.datacube import Datacube
import matplotlib
import math
from numpy import *
import scipy.optimize
from quantum.qulib import *
import sys
matplotlib.use("module://pyview.gui.mpl.backend_static")
from matplotlib.pyplot import *

data1 = Datacube()
data1.loadtxt("IQ tomography-11")

data2 = Datacube()
data2.loadtxt("IQ tomography-12")

data3 = Datacube()
data3.loadtxt("IQ tomography-13")

data_array = [data1,data2,data3]
matrix_array = []

for i in range(0,len(data_array)):
    
    data = data_array[i]
    n = int(sqrt(len(data)))

    m = zeros((n,n))

    for i in range(0,n*n):
        m[i%n,int(i/n)]=data["px1"][i]
        
    matrix_array.append(m)

def IQ_sequence(initial_state,I,Q,extra_angle):
    A=sqrt(I*I+Q*Q)
    angle = math.atan2(Q,I)+extra_angle
    if I == 0 and Q == 0:
        return initial_state
    return rotn(A,[cos(angle),sin(angle),0])*initial_state


def generate_initial_state(angle,x,y):
    n = sqrt(x*x+y*y)
    if x == 0 and y == 0:
        print "zero!"
        return matrix([[1],[0]])
    return rotn(angle,[x/n,y/n,0.])*matrix([[1],[0]])

initial_states = [generate_initial_state(math.pi,1,0),generate_initial_state(math.pi/2.0,1,0),generate_initial_state(math.pi/2.0,0,1)]

simulated_array = []

def generate_simulation(initial_state,n,AI,AQ,c0,c1,extra_angle):
    m = zeros((n,n))
    A = linspace(-10,10,n)
    for i in range(0,n):
        for q in range(0,n):
            new_state = IQ_sequence(initial_state,A[i]*AI,A[q]*AQ,extra_angle)
            m[i,q] = new_state[1,0]*conj(new_state[1,0])*(c1-c0)+c0
    return m

for initial_state in initial_states:
    simulated_array.append(generate_simulation(initial_state,100,1,1,0,1,0))

def error_function(measured_data,simulated_data):
    n = norm(measured_data-simulated_data)
    return n

def generate_state_and_simulation(params,n):
    angle = params[0]
    x = params[1]
    y = params[2]
    AI = params[3]
    AQ = params[4]
    c0 = params[5]
    c1 = params[6]
    extra_angle = params[7]
    initial_state = generate_initial_state(angle,x,y)
    simulation = generate_simulation(initial_state,n,AI,AQ,c0,c1,extra_angle)
    return simulation

def data_error_function(params,data):
    n = len(data)
    simulation = generate_state_and_simulation(params,n)
    return error_function(simulation,data)

initial_parameters_array = (
    [math.pi,1,0,1,1,0.1,0.9,0.1],
    [math.pi/2.,0,1,1,1,0.1,0.9,-0.4],
    [math.pi/2.,1,0,1,1,0.1,0.9,-0.4]
)

optimized_array = []
optimal_parameters_array = []

for i in range(0,len(matrix_array)):
    m = matrix_array[i]
    initial_parameters = initial_parameters_array[i]
    optimal_parameters = initial_parameters
    optimal_parameters = scipy.optimize.fmin(data_error_function,initial_parameters,args = (m,))
    print "Phase: %g, Angle: %g" % (optimal_parameters[0]*180.0/math.pi,math.atan2(optimal_parameters[1],optimal_parameters[2])*180./math.pi)
    print optimal_parameters
    optimized_array.append(generate_state_and_simulation(optimal_parameters,len(m)))
    optimal_parameters_array.append(optimal_parameters)

figure(1,figsize=(6,6))

for i in range(0,len(matrix_array)):
    subplot(3,3,i+1)
    cla()
    extent = (-1,1,-1,1)
    imshow(matrix_array[i],aspect = 1,interpolation = 'nearest',vmin = 0,vmax = 1,extent = extent)
    axvline(0,ls='--',color = 'black')
    axhline(0,ls='--',color = 'black')
    xticks([])
    yticks([])
    subplot(3,3,i+4)
    imshow(optimized_array[i],aspect = 1,interpolation = 'nearest',vmin = 0,vmax = 1,extent = extent)
    rotation_angle = -optimal_parameters_array[i][7]
    plot([cos(rotation_angle)*1.,cos(rotation_angle)*-1.],[sin(rotation_angle)*1.,sin(rotation_angle)*-1.],ls = '--',color = 'black')
    plot([-sin(rotation_angle)*1.,-sin(rotation_angle)*-1.],[cos(rotation_angle)*1.,cos(rotation_angle)*-1.],ls = '--',color = 'black')
    xlim(-1,1)
    ylim(-1,1)
#    axvline(0,ls='--',color = 'black')
#    axhline(0,ls='--',color = 'black')
    xticks([])
    yticks([])
    subplot(3,3,i+7)
    imshow(optimized_array[i]-matrix_array[i],aspect = 1,interpolation = 'nearest',vmin = -0.25,vmax = 0.25,extent = extent)
    plot([cos(rotation_angle)*1.,cos(rotation_angle)*-1.],[sin(rotation_angle)*1.,sin(rotation_angle)*-1.],ls = '-_-',color = 'red')
    plot([-sin(rotation_angle)*1.,-sin(rotation_angle)*-1.],[cos(rotation_angle)*1.,cos(rotation_angle)*-1.],ls = '-_-',color = 'black')
    axvline(0,ls='--',color = 'black')
    axhline(0,ls='--',color = 'black')
    xticks([])
    yticks([])
show()


sys.stdin.readline()