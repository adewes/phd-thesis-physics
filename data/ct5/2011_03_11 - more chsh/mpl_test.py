from matplotlib.pyplot import *
from pyview.ide.mpl.backend_agg import *
import time
cnt = 0
while True:
	figure("tset")
	time.sleep(0.1)
	plot([1,2,3,cnt])
	xlabel("tset")
	ylabel("another one")
	legend(["tester"])
	title("This is just a tset")
	cnt+=1
	draw()