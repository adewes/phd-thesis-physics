import yaml
import os
import os.path
import matplotlib
matplotlib.use("module://pyview.gui.mpl.backend_static")
from matplotlib.pylab import *

files = os.listdir(os.getcwd())

freqs = []
t_pis = []

for filename in files:
    if filename.startswith("T1_survey_-_Qubit_2-4_Rabi__coil_=") and filename.endswith(".par"):
        f = open(filename,"r")
        content = f.read()
        values = yaml.load(content)
        if "rabiParameters" in values["parameters"]:
            t_pi = values["parameters"]["rabiParameters"][1]
            freq = values["parameters"]["qubit2mwg"]["frequency"]
            t_pis.append(t_pi)
            freqs.append(freq)
            
figure(1)
clf()
plot(freqs,t_pis)
show()

import sys
sys.stdin.readline()