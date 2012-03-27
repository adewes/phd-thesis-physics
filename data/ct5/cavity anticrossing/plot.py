#Set the working path to your data directory before executing this script!
import matplotlib
matplotlib.use('module://pyview.gui.mpl.backend')
from matplotlib.pyplot import *
from numpy import *
import os
files = os.listdir(".")
print files
import re
dataColumn = 2
data = []
voltages = []
frequencies = []
cnt = 0
for file in files:
	print file
	match = re.search('cavity-1-vcoil=([\-\d\.]+)-2.txt$',file)
	if match != None:
		newData = genfromtxt(file,skiprows = 1)
		if len(newData) == 1600:
			print "Appending..."
			data.append(newData)
			voltages.append(float(match.groups(0)[0]))
print "Done"
print voltages
##
import math
anticrossing = zeros((0,2))
cnt = 0
for i in range(0,len(data)):
	print "Correcting dataset %d" % i
	for j in range(0,len(data[i])):
		if data[i][j,dataColumn]<180:
			data[i][j,dataColumn]+=360
		if j > 0:
			if math.fabs(data[i][j,dataColumn]-data[i][j-1,dataColumn]) > math.fabs(data[i][j,dataColumn]-data[i][j-1,dataColumn]+360):
				data[i][j,dataColumn] = data[i][j,dataColumn]+360
			elif math.fabs(data[i][j,dataColumn]-data[i][j-1,dataColumn]) > math.fabs(data[i][j,dataColumn]-data[i][j-1,dataColumn]-360):
				data[i][j,dataColumn] = data[i][j,dataColumn]-360
			if math.fabs(data[i][j,dataColumn]-data[i][j-1,dataColumn])>180:
				anticrossing.resize((cnt+1,2))
				anticrossing[cnt,0]=voltages[i]
				anticrossing[cnt,1]=data[i][j,0]
				cnt+=1
print anticrossing
##
figure(14)
cla()
scatter(anticrossing[:,0],anticrossing[:,1])
savetxt("anticrossing-cavity-1.txt",anticrossing)
show()
##
xmin = -1
xmax = -1
ymin = -1
ymax = -1
for i in range(0,len(data)):
	if i == 0:
		xmin = voltages[i]
		xmax = voltages[i]
	if voltages[i] > xmax:
		xmax = voltages[i]
	if voltages[i] < xmin:
		xmin = voltages[i]
	for j in range(0,len(data[i][:,0])):
		if (i == 0 and j == 0):
			ymax = data[i][j,0]
			ymin = data[i][j,0]
		else:
			if data[i][j,0]<ymin:
				ymin = data[i][j,0]
			if data[i][j,0]>ymax:
				ymax = data[i][j,0]

print xmax,xmin

ybins = len(data[0][:,0])
xbins = len(data)-1

print xbins,ybins

dataMatrix = zeros((xbins,ybins))
samples = zeros((xbins,ybins))
for i in range(0,len(data)):
	x = int((voltages[i]-xmin)/(xmax-xmin)*(xbins-1))
	if len(data[i]) == ybins:
		print "Generating matrix column %d" % i
		dataMatrix[x,:] = data[i][:,dataColumn]

dataMatrix = transpose(dataMatrix)

##
m = len(dataMatrix)
n = len(dataMatrix[0])
newDataMatrix = zeros((m,n))
for i in arange(0,m,1):
	for j in arange(0,n,1):
		sum1 = 0
		sum2 = 0
		sum3 = 0
		if dataMatrix[i,j] < 0:
			dataMatrix[i,j]+=360
		if dataMatrix[i,j] > 360:
			dataMatrix[i,j]-=360
##
savetxt("qubit-1-anticrossing-matrix-xmin=%g-xmax=%g-ymin=%g-ymax=%g.txt" % (xmin,xmax,ymin,ymax),dataMatrix)
dataMatrixQubit1 = dataMatrix
##
figure(12)
clf()
cla()
hsv()
imshow(dataMatrix[:,] ,aspect = 'auto',interpolation = 'nearest',origin = 'lower',extent = (xmin,xmax,ymin/1e9,ymax/1e9))
show()

xlabel("$V_{coil}$ [V]")
##
figure(13)
cla()
scatter(data[20][:,0],data[20][:,2])
##
figure(33)
clf()
i=84
#plot(dataMatrix[i][:,0],dataMatrix[:,i])
plot(data[i][:,0],data[i][:,2])
show()
