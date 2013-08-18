from experimental_chi_matrix import chi

print chi

import matplotlib

matplotlib.use("module://pyview.gui.mpl.backend_static")

from matplotlib.pylab import *
from quantum.plotting import *
from quantum.qulib import *
#figure(1)
#plotDensityMatricesContour([chi],annotate = False)
#show()
#import sys
#sys.stdin.readline()

eigvals,eigvecs = eigh(chi)

print eigvals

E = []

eigvecs = transpose(eigvecs)

sigmas = [idatom,sigmax,1j*sigmay,sigmaz]

for i in range(0,4):
	for j in range(0,4):
		E.append(tensor(sigmas[i],sigmas[j]))

kraus_operators = []
for i in range(0,len(eigvecs)):
    eigenvector = eigvecs[i]
    op = matrix(zeros((4,4),dtype = complex128))
    for j in range(0,16):
        print eigenvector[0,j]
        op+=-E[j]*eigenvector[0,j]*eigvals[i]
    kraus_operators.append(op)
    
figure(1,figsize=(16*0.7,4*0.7))
for i in range(12,16):
    subplot(1,4,i-11)
    if i == 12:
        labels = ["00","01","10","11"]
    else:
        labels = []
    plotDensityMatricesContour([kraus_operators[i]],annotate = False,labels = labels)
    title("$\lambda=$ %.3f" % eigvals[i])
show()
swap = 1/sqrt(2)*matrix([[sqrt(2),0,0,0],[0,1,-1j,0],[0,-1j,1,0],[0,0,0,sqrt(2)]])
print norm(swap-kraus_operators[15])
savefig("process_kraus_operators.pdf")
import sys
sys.stdin.readline()
