fitfunc = lambda p,x: p[1]*sin(p[2]+x/180.0*math.pi)
errfunc = lambda p, x, y,ff: numpy.linalg.norm((ff(p,x)-y))

best_value = None
best_data = None

fitnessValues = dict()

for i in range(0,len(tomographySurvey)):
	parent = tomographySurvey.childrenAt(i)[0]
	spins = parent.allChildren()[0]
	
	
	ps = [0,0.5,0]
	p1s = scipy.optimize.fmin(errfunc, ps,args=(spins["phi"],spins["chsh"],fitfunc),maxfun = 1e5,maxiter = 1e5)
	spins.createColumn("chsh_fit",fitfunc(p1s,spins["phi"]))
	
	distance = max(abs(spins["chsh"]-spins["chsh_fit"]))

	print distance

	fitnessValues[i] = distance

	if best_value == None or distance < best_value:
		best_value = distance
		best_data = spins

	tomographySurvey.setAt(i,distance = distance)

#tomographySurvey.sortBy("distance")
##
cnt = 1
for i in sorted(zip(fitnessValues.values(),fitnessValues.keys())):
	print i[1]
	cube = tomographySurvey.childrenAt(i[1])[0]
	if 'originalName' in cube.parameters():
		cube.setName(cube.parameters()["originalName"])
	else:
		cube.parameters()["originalName"] = cube.name()
	print cube.name()
	cube.setName(cube.name()+(" - %d " % cnt))
	cnt += 1