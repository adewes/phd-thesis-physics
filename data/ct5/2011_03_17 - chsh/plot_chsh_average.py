chsh_avg = None

cnt = 0

phis = None

figure("average")
cla()
ioff()
for i in range(0,len(tomographySurvey)):
	parent = tomographySurvey.childrenAt(i)[0]
	spins = parent.allChildren()[0]
	if phis == None:
		phis = spins["phi"]
	if chsh_avg == None:
		chsh_avg = spins["chsh"]
	elif len(spins["chsh"]) == len(chsh_avg):
		chsh_avg+= spins["chsh"]
	cnt+=1
	plot(spins["phi"],spins["chsh"])
chsh_avg/=float(cnt)
plot(phis,chsh_avg)
draw()
##
cla()
scatter(phis,chsh_avg)
data = tomographySurvey.childrenAt(fitnessRange[5][1])[0].allChildren()[0]
plot(phis,sin(phis/180.0*math.pi+math.pi*0.79)*2.5)
scatter(data["phi"],data["chsh"],color = 'red')
plot(data["phi"],data["chsh_fit"])
xlabel("phi")
ylabel("chsh")
title("2011/03/17 - chsh survey")