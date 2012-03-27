import matplotlib
matplotlib.use('module://pyview.gui.mpl.backend')

from numpy import *
from matplotlib.pyplot import *	
from matplotlib.patches import *
import sys
sys.path.append(r'l:\python')
##
from qubit_setup.scripts.qulib import *
transferMatrix = array([
		[0.2,0.4,0.1,0.3],
		[0.5,0.2,0.2,0.1],
		[0.,0.3,0.6,0.1],
		[0.2,0.1,0.,0.7]
	])
	
	
process = matrix([
		[1,0,0,0],
		[0,1/sqrt(2.),1j/sqrt(2),0],
		[0,1j/sqrt(2),1/sqrt(2),0],
		[0,0,0,1]
	])

phi_in = gg
phi_in = phi_in/norm(phi_in)
rho_in = adjoint(phi_in)*phi_in

Es= []
ps = [sigmax,1j*sigmay,sigmaz,idatom]

for i in range(0,len(ps)):
	for j in range(0,len(ps)):
		Es.append(tensor(ps[i],ps[j]))

import numpy.linalg

mappingMatrix = matrix(zeros((len(Es),len(Es)),dtype = complex128))
transferMatrix = zeros((len(Es),len(Es)),dtype = complex128)

for i in range(0,len(Es)):
	mappingMatrix[i,:] = ravel(Es[i])

inverseMappingMatrix = numpy.linalg.inv(mappingMatrix)

for i in range(0,len(Es)):
	print adjoint(process)*Es[i]*process
	transferMatrix[i] = ravel(ravel(adjoint(process)*Es[i]*process)*inverseMappingMatrix)

print "Input:",rho_in	
print "Output:",reduce(lambda x,y:x+y,map(lambda x:x[0]*Es[x[1]],zip(ravel(ravel(adjoint(process)*rho_in*process)*inverseMappingMatrix),range(0,16))))

##
figure(5)
clf()
subplot(121)
imshow(real(transferMatrix),interpolation = 'nearest')
subplot(122)
imshow(imag(transferMatrix),interpolation = 'nearest')
show()

##
import numpy.random
#transferMatrix = numpy.random.rand(16,16)

transferMatrix = abs(transferMatrix)

def plotTransferMatrix(transferMatrix,xmargin = 0.02,ymargin = 0.02,width = 0.4,fig = 1,colors = ['blue','green','red','cyan']):
	figure(fig)
	clf()
	ax = axes()
	print ax
	xticks([])
	axis = twiny()
	xticks(arange(0,len(transferMatrix))+0.5,["test"]*len(transferMatrix))
	yticks(arange(0,len(transferMatrix[0]))+0.5,["test"]*len(transferMatrix[0]))
	ax.xaxis.set_major_locator(NullLocator())
	ax.yaxis.set_major_locator(NullLocator())
	axis.xaxis.set_major_locator(NullLocator())
	for column in range(0,len(transferMatrix)):
		columnSum = 0
		nonZeroColumns = filter(lambda x: True if x > 0 else False,transferMatrix[column,:])
		columnWidth = sum(nonZeroColumns)*width+xmargin*(len(nonZeroColumns)-1)
		for row in range(0,len(transferMatrix[column])):
			currentValue = transferMatrix[column,row]
			nonZeroRows = filter(lambda x: True if x else False,transferMatrix[:,row])
			rowHeight = sum(nonZeroRows)*width+ymargin*(len(nonZeroRows)-1)
			if currentValue > 0:
				x = column+0.5-columnWidth/2.+columnSum*width+sum(map(lambda x:1 if x>0 else 0,transferMatrix[column,:row]))*xmargin
				dx = currentValue*width
				y = len(transferMatrix[0])-row-0.5+rowHeight/2.-sum(transferMatrix[:column,row])*width-sum(map(lambda x:1 if x>0 else 0,transferMatrix[:column,row]))*ymargin
				dy = dx
				c = colors[row%len(colors)]
				p1 = Polygon([(x+dx,len(transferMatrix[0])),(x+dx,y-dy),(dx/2.,y-dy),(0,y-dy/2.),(dx/2.,y),(x,y),(x,len(transferMatrix[0]))],color = c,zorder = -column+row,ls = 'solid',lw = 0,ec = c)
				gca().add_patch(p1)
				columnSum+=currentValue
	xlim(-xmargin,len(transferMatrix)+xmargin)
	ylim(-ymargin,len(transferMatrix[0])+ymargin)
	show()
	
plotTransferMatrix(transferMatrix,fig = 4)
fig = figure(4)
fig.set_size_inches((10,10))
savefig("test.pdf")
##
figure(10)
clf()
results = zeros((4,4))
results[0,:] = [0.666625,0.126875,0.127875,0.078625]
results[1,:] = [0.19225,0.5535,0.106,0.14825]
results[2,:] = [0.18775,0.070625,0.615375,0.12625]
results[3,:] = [0.122375,0.122125,0.238875,0.516625]
for i in range(0,4):
	subplot(1,4,i+1)
	bar([1,2,3,4],results[i,:],align = 'center',color = ['blue','green','red','cyan'])
	ylim(0,1.0)
	xticks([])
	yticks([])
	yticks(arange(0,1.5,0.5),[""]*3)
	axhline(0.5,ls = 'dashed',color = 'grey')
	xticks([1,2,3,4],["00","01","10","11"])
subplot(1,4,1)
yticks(arange(0,1.5,0.5),arange(0,1.5,0.5))
show()