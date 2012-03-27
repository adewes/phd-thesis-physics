##Start the data manager
import sys
from pyview.gui.coderunner import *
from pyview.gui.datamanager import *
reload(sys.modules["pyview.gui.datamanager"])
from pyview.gui.datamanager import *

def startInstrumentsPanel():
	
	global manager
	
	manager = DataManager(globals = gv)
	manager.show()

execInGui(startInstrumentsPanel)

##
from matplotlib.pyplot import *
from numpy import *
from pyview.lib.datacube import Datacube
cube = Datacube()
cube.loadtxt("State Tomography of Swap vs Swap Duration.txt")
##
print cube.structure()
##

def smooth(x,window_len=11,window='hanning'):
    """smooth the data using a window with requested size.
    
    This method is based on the convolution of a scaled window with the signal.
    The signal is prepared by introducing reflected copies of the signal 
    (with the window size) in both ends so that transient parts are minimized
    in the begining and end part of the output signal.
    
    input:
        x: the input signal 
        window_len: the dimension of the smoothing window; should be an odd integer
        window: the type of window from 'flat', 'hanning', 'hamming', 'bartlett', 'blackman'
            flat window will produce a moving average smoothing.

    output:
        the smoothed signal
        
    example:

    t=linspace(-2,2,0.1)
    x=sin(t)+randn(len(t))*0.1
    y=smooth(x)
    
    see also: 
    
    numpy.hanning, numpy.hamming, numpy.bartlett, numpy.blackman, numpy.convolve
    scipy.signal.lfilter
 
    TODO: the window parameter could be the window itself if an array instead of a string   
    """

    if x.ndim != 1:
        raise ValueError, "smooth only accepts 1 dimension arrays."

    if x.size < window_len:
        raise ValueError, "Input vector needs to be bigger than window size."


    if window_len<3:
        return x


    if not window in ['flat', 'hanning', 'hamming', 'bartlett', 'blackman']:
        raise ValueError, "Window is on of 'flat', 'hanning', 'hamming', 'bartlett', 'blackman'"


    s=numpy.r_[2*x[0]-x[window_len-1::-1],x,2*x[-1]-x[-1:-window_len:-1]]
    #print(len(s))
    if window == 'flat': #moving average
        w=numpy.ones(window_len,'d')
    else:
        w=eval('numpy.'+window+'(window_len)')

    y=numpy.convolve(w/w.sum(),s,mode='same')
    return y[window_len:-window_len+1]

figure("pauli vs time")
cla()
clf()
ioff()
cnt = 0
ax = gca()
spinLabels = ["xi","yi","zi","ix","iy","iz","xx","xy","xz","yx","yy","yz","zx","zy","zz"]
tickLabels = map(lambda x:x.upper(),spinLabels)
ys = []
for spin in spinLabels:
	print spin
	cnt += 1
	y1 = smooth(gv.spins.column(spin))
	y2 = cnt*1.5
	ys.append(y2)
	if cnt < 4:
		scolor = (0.35,0,0)
		color = 'red'
	elif cnt < 7:
		scolor = (0,0.35,0)
		color = 'green'
	else:
		scolor = (0,0,0.35)
		color = 'blue'
	plot(gv.spins.column("t"),y1 + y2,color = scolor,lw = 2)
	plot(gv.spinsSimulation.column("t"),gv.spinsSimulation.column(spin)+y2,color = 'black',ls = 'dashed',lw = 2)
	ax.fill_between(gv.spins.column("t"),y1+y2,y2,color = color)

print "Done!"
ylim(ys[0]-1,ys[-1]+1)
xlim(0,600)
xlabel(r"swap duration [ns]")
yticks(ys,tickLabels)
show()
##
importModule("scripts.state_tomography.plot_density_matrix")
from scripts.state_tomography.plot_density_matrix import *

state = tensor(gs,es)+1j*tensor(es,gs)

state = state / norm(state)

rho = adjoint(state)*state

ops = generateCombinations([idatom,sigmax,sigmay,sigmaz],lambda x,y:tensor(x,y),2)

values = []

for op in ops:
	values.append(trace(rho*op))

from qulib import *
from pyview.ide.mpl.backend_agg import *
figure("new",(100,10))
cla()
plotPauliSet(gv.spins,row = 3,fill = True,lw = 0.)
plotPauliSet(densityMatrix = rho,fill = False)
ylim(-1.1,1.1)
show()
##
densityMatrix = zeros((4,4),dtype = complex128)

for i in range(0,4):
	for j in range(0,4):
		densityMatrix[i,j] = gv.densityMatrices[str(i)+str(j)][2]
		

plotDensityMatrix(densityMatrix,figureName = "rhospin")
show()