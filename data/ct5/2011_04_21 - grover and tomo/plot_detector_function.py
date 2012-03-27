from config.startup import *

data = gv.crosstalk.children()[0]

m = matrix(data.parameters()["qubit1"]["detectorFunction"])

detector1 = matrix([[data.parameters()["qubit1"]["readout.p00"],1.0-data.parameters()["qubit1"]["readout.p11"]],[1.0-data.parameters()["qubit1"]["readout.p00"],data.parameters()["qubit1"]["readout.p11"]]])
detector2 = matrix([[data.parameters()["qubit2"]["readout.p00"],1.0-data.parameters()["qubit2"]["readout.p11"]],[1.0-data.parameters()["qubit2"]["readout.p00"],data.parameters()["qubit2"]["readout.p11"]]])
dm = tensor(detector1,detector2)

crosstalkMatrix = m*inv(dm)

plotDensityMatrix(crosstalkMatrix,figureName = "crosstalkMatrix")
show()

savetxt("crosstalk_matrix.txt",crosstalkMatrix)
savetxt("visibility_matrix.txt",dm)
savetxt("detection_matrix.txt",m)
