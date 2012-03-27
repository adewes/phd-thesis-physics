importModule("pyview.lib.datacube")
cube = Datacube()
cube.reloadClass()
cube.__init__()
for i in range(0,100,1):
	cube.set(x = i, y = i*i,z = i*i*i)
	cube.commit()
cube.savetxt("all_in_one.txt",allInOneFile = True,overwrite = True)