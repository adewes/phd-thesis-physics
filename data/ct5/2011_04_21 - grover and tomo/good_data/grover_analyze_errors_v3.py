import matplotlib
matplotlib.rcParams["font.size"] = 16

def convertToDensityMatrix(datacube,i,d = 4):
	matrix = []
	for row in range(0,4):
		row_values = []
		matrix.append(row_values)
		for column in range(0,4):
			row_values.append(complex(datacube[str(row)+str(column)][i]))
	return matrix

#matrices = []
#for i in range(0,len(gv.grover)):
#	matrices.append(convertToDensityMatrix(gv.grover,i))
#print matrices
##

from quantum.qulib import *
from quantum.plotting import *
import scipy.linalg

Er1 = lambda gamma:matrix([[1,0],[0,sqrt(1-gamma)]],dtype=complex128)
Er2 = lambda gamma:matrix([[0,sqrt(gamma)],[0,0]],dtype=complex128)
Eg1 = lambda gamma:matrix([[1,0],[0,sqrt(1-gamma)]],dtype=complex128)
Eg2 = lambda gamma:matrix([[0,0],[0,sqrt(gamma)]],dtype=complex128)

gamma_t = lambda gamma,t:1.-exp(-t*gamma)

apply_process = lambda rho,E1,E2:E1*rho*adjoint(E1)+E2*rho*adjoint(E2)

ao = lambda o,rho:o*rho*adjoint(o)

relax = lambda rho,gamma,t:apply_process(rho,Er1(gamma_t(gamma,t)),Er2(gamma_t(gamma,t)))

relax_2_1 = lambda rho,gamma1,t:apply_process(rho,tensor(Er1(gamma_t(gamma1,t)),idatom),tensor(Er2(gamma_t(gamma1,t)),idatom))
relax_2_2 = lambda rho,gamma2,t:apply_process(rho,tensor(idatom,Er1(gamma_t(gamma2,t))),tensor(idatom,Er2(gamma_t(gamma2,t))))
relax_2 = lambda rho,gamma1,gamma2,t:relax_2_1(relax_2_2(rho,gamma1,t),gamma2,t)

rotation = lambda angle,n = (1,0,0) : matrix([[cos(angle/2.)-1j*n[2]*sin(angle/2.),(-1j*n[0]-n[1])*sin(angle/2)],[(-1j*n[0]+n[1])*sin(angle/2),cos(angle/2)+1j*n[2]*sin(angle/2)]],dtype=complex128)

iswap = lambda phi,delta : matrix([[1,0,0,0],[0,cos(phi)-1j*delta/sqrt(1+delta*delta)*sin(phi),1j/sqrt(1+delta*delta)*sin(phi),0],[0,1j/sqrt(1+delta*delta)*sin(phi),cos(phi)+1j*delta/sqrt(1+delta*delta)*sin(phi),0],[0,0,0,1]],dtype=complex128)

rot_phi = lambda angle,phase : rotation(angle,(cos(phase),sin(phase),0))
rot_z = lambda angle : rotation(angle,(0,0,1))

dephase_2_1 = lambda rho,gamma1,t:apply_process(rho,tensor(Eg1(gamma_t(gamma1,t)),idatom),tensor(Eg2(gamma_t(gamma1,t)),idatom))
dephase_2_2 = lambda rho,gamma2,t:apply_process(rho,tensor(idatom,Eg1(gamma_t(gamma2,t))),tensor(idatom,Eg2(gamma_t(gamma2,t))))
dephase_2 = lambda rho,gamma1,gamma2,t:dephase_2_1(dephase_2_2(rho,gamma1,t),gamma2,t)

##Grover density matrices, as given in:
#E:\cygwin\home\adewes\thesis\data\ct5\2011_04_21 - grover and tomo\good_data\grover - maximum likelihood estimated density matrices of run 1.par
#The matrices correspond to quantum state after step 1,2,3,4,5 of the Grover algorithm for the states 00,01,10 and 11.
#matrices = [[[(0.277717003178-1.4782827649e-18j), (0.248720259174-0.0479223051138j), (0.243234413481-0.0252981556514j), (0.217361643952-0.0832260226772j)], [(0.248720259174+0.0479223051138j), (0.242169702828-1.28906510503e-18j), (0.230292303658+0.0181348863685j), (0.205449342684-0.0225580715578j)], [(0.243234413481+0.0252981556514j), (0.230292303658-0.0181348863685j), (0.256402436182-2.85526081365e-18j), (0.206132601145-0.0553914249732j)], [(0.217361643952+0.0832260226772j), (0.205449342684+0.0225580715578j), (0.206132601145+0.0553914249732j), (0.223710857812+5.62260868359e-18j)]], [[(0.323017477798-8.4051900283e-19j), (-0.0226700791735+0.206639192754j), (-0.0474527328796+0.271651484849j), (0.167236803214+0.022331014302j)], [(-0.0226700791735-0.206639192754j), (0.197899436852-5.14951198484e-19j), (0.206435121312-0.00291658347138j), (0.00180578839165-0.164862172013j)], [(-0.0474527328796-0.271651484849j), (0.206435121312+0.00291658347138j), (0.275682370651+2.75209793153e-18j), (-0.00365998383998-0.184097914936j)], [(0.167236803214-0.022331014302j), (0.00180578839165+0.164862172013j), (-0.00365998383998+0.184097914936j), (0.2034007147-1.39662773022e-18j)]], [[(0.349040759194+0j), (-0.226302910115-0.0657672681072j), (-0.184235058152-0.059381422711j), (-0.203539472688-0.00167881672382j)], [(-0.226302910115+0.0657672681072j), (0.239147130162+0j), (0.16087704702+0.0422993881323j), (0.167979356386+0.000204237509748j)], [(-0.184235058152+0.059381422711j), (0.16087704702-0.0422993881323j), (0.224097584642+0j), (0.163971547364+0.0129738288716j)], [(-0.203539472688+0.00167881672382j), (0.167979356386-0.000204237509748j), (0.163971547364-0.0129738288716j), (0.187714526002+0j)]], [[(0.391409720995+8.48734539669e-20j), (0.00410950509939-0.21081868786j), (0.0187288947002-0.159200553913j), (-0.141888557981-0.00657227461839j)], [(0.00410950509939+0.21081868786j), (0.248280609489+5.38372752389e-20j), (0.162785143225+0.0535921836272j), (0.0154053851236-0.131991195984j)], [(0.0187288947002+0.159200553913j), (0.162785143225-0.0535921836272j), (0.219777380926+4.76566227727e-20j), (-0.00238754118138-0.101971370332j)], [(-0.141888557981+0.00657227461839j), (0.0154053851236+0.131991195984j), (-0.00238754118138+0.101971370332j), (0.140532288589-1.86367351979e-19j)]], [[(0.676314789692-8.06588160695e-19j), (-0.0547649822398+0.147104536213j), (-0.0514328790472+0.0803112341581j), (-0.00425507192827-0.0114732988693j)], [(-0.0547649822398-0.147104536213j), (0.120596165334-1.43825686893e-19j), (0.0207806694769+0.0213122855972j), (-0.0370840018113+0.0410357855819j)], [(-0.0514328790472-0.0803112341581j), (0.0207806694769-0.0213122855972j), (0.110926974842+1.92966657923e-19j), (-0.000978019772056+0.0704594745651j)], [(-0.00425507192827+0.0114732988693j), (-0.0370840018113-0.0410357855819j), (-0.000978019772056-0.0704594745651j), (0.0921620701321+7.57447189665e-19j)]], [[(0.288621006504-2.08144598898e-18j), (0.254415619066-0.0459844520245j), (0.247067892548-0.0292612227046j), (0.219947625382-0.0844594737492j)], [(0.254415619066+0.0459844520245j), (0.246321887874-1.77639774639e-18j), (0.22487210382+0.0253618041908j), (0.204736187742-0.0220616529575j)], [(0.247067892548+0.0292612227046j), (0.22487210382-0.0253618041908j), (0.246619821693-9.30111925028e-19j), (0.203239807632-0.0532386620155j)], [(0.219947625382+0.0844594737492j), (0.204736187742+0.0220616529575j), (0.203239807632+0.0532386620155j), (0.218437283929+4.7879556604e-18j)]], [[(0.324161269994+0j), (-0.011618810831+0.209230619758j), (-0.0119539455745+0.264599938364j), (0.173439641448+0.02392573071j)], [(-0.011618810831-0.209230619758j), (0.202578727369+0j), (0.197090127894-0.0255650500769j), (-0.00156564608673-0.160822564848j)], [(-0.0119539455745-0.264599938364j), (0.197090127894+0.0255650500769j), (0.2759344467+0j), (-0.00673486229983-0.184396129846j)], [(0.173439641448-0.02392573071j), (-0.00156564608673+0.160822564848j), (-0.00673486229983+0.184396129846j), (0.197325555938+0j)]], [[(0.290751862136-1.00874816186e-18j), (0.197576778126+0.0685752309767j), (-0.206470788038-0.0677680997736j), (0.158641990977-0.0189745881923j)], [(0.197576778126-0.0685752309767j), (0.257372904446-8.92941638847e-19j), (-0.186806702562-0.0256885679343j), (0.154398372981-0.044410576234j)], [(-0.206470788038+0.0677680997736j), (-0.186806702562+0.0256885679343j), (0.298675433076+2.43320838105e-18j), (-0.184423711272+0.0463924645799j)], [(0.158641990977+0.0189745881923j), (0.154398372981+0.044410576234j), (-0.184423711272-0.0463924645799j), (0.153199800342-5.31518580337e-19j)]], [[(0.432799127213+3.00314722544e-18j), (-0.0446689339182-0.130531979597j), (0.0336712656174+0.184871490353j), (0.122267071991-0.0508687033958j)], [(-0.0446689339182+0.130531979597j), (0.168235408194+1.16736764834e-18j), (-0.122523460576-0.0648856430539j), (-0.000786952233997+0.0771348968226j)], [(0.0336712656174-0.184871490353j), (-0.122523460576+0.0648856430539j), (0.273083501018-1.57454951148e-18j), (-0.0589975349438-0.144785106247j)], [(0.122267071991+0.0508687033958j), (-0.000786952233997-0.0771348968226j), (-0.0589975349438+0.144785106247j), (0.125881963575-2.59596536229e-18j)]], [[(0.108876714263+9.44354961098e-20j), (-0.0182342255286+0.0658362076538j), (-0.0906862960555+0.0313177706588j), (-0.0352022402927-0.0240616388672j)], [(-0.0182342255286-0.0658362076538j), (0.0986981123492+8.56069662634e-20j), (0.0533583927598+0.0352137365698j), (-0.0399977354455+0.0611146313827j)], [(-0.0906862960555-0.0313177706588j), (0.0533583927598-0.0352137365698j), (0.635691364224+5.51374366498e-19j), (-0.0123831470486+0.218829182791j)], [(-0.0352022402927+0.0240616388672j), (-0.0399977354455-0.0611146313827j), (-0.0123831470486-0.218829182791j), (0.156733809163-7.31416828871e-19j)]], [[(0.289342152533-3.07315677349e-19j), (0.248778716951-0.0492608575249j), (0.253824349633-0.0272288707884j), (0.224599880627-0.089389795834j)], [(0.248778716951+0.0492608575249j), (0.238178673521-2.52973995466e-19j), (0.231979774805+0.0174071622451j), (0.205567308633-0.0222416169766j)], [(0.253824349633+0.0272288707884j), (0.231979774805-0.0174071622451j), (0.246650718678+1.22499370557e-18j), (0.209056122341-0.0416574596142j)], [(0.224599880627+0.089389795834j), (0.205567308633+0.0222416169766j), (0.209056122341+0.0416574596142j), (0.225828455269-6.64704032757e-19j)]], [[(0.329448575601-1.14300435644e-18j), (-0.0549773184933+0.173734486895j), (-0.0867316838417+0.273638898616j), (0.154840482357+0.0972360489541j)], [(-0.0549773184933-0.173734486895j), (0.193688406755-6.71991652445e-19j), (0.203360852198-0.0318492400956j), (0.0449070710309-0.152030991447j)], [(-0.0867316838417-0.273638898616j), (0.203360852198+0.0318492400956j), (0.284379591804+2.48280704397e-18j), (0.0586605745536-0.169619181118j)], [(0.154840482357-0.0972360489541j), (0.0449070710309+0.152030991447j), (0.0586605745536+0.169619181118j), (0.192483425841-6.67811035085e-19j)]], [[(0.354387223498+0j), (-0.204209393526-0.120267540146j), (0.159301084887+0.110847991964j), (0.126344970011+0.132771027517j)], [(-0.204209393526+0.120267540146j), (0.23058360085+0j), (-0.172597268561-0.00293859583j), (-0.18978793476-0.00767300632125j)], [(0.159301084887-0.110847991964j), (-0.172597268561+0.00293859583j), (0.208817689959-1.73472347598e-18j), (0.16441917258+0.0520773830112j)], [(0.126344970011-0.132771027517j), (-0.18978793476+0.00767300632125j), (0.16441917258-0.0520773830112j), (0.206211485694+1.73472347598e-18j)]], [[(0.396024073839-5.15244193456e-19j), (-0.0784850026609+0.15229582638j), (0.0565243010776-0.205843339809j), (0.098826405083+0.0719783649678j)], [(-0.0784850026609-0.15229582638j), (0.193966649387-2.52358875186e-19j), (-0.141781296753+0.0158636911273j), (0.0141900110389-0.0988986574604j)], [(0.0565243010776+0.205843339809j), (-0.141781296753-0.0158636911273j), (0.271073317889+9.48364670793e-19j), (-0.0537316362809+0.158492240962j)], [(0.098826405083-0.0719783649678j), (0.0141900110389+0.0988986574604j), (-0.0537316362809-0.158492240962j), (0.138935958886-1.80761602152e-19j)]], [[(0.138556454969+0j), (-0.108751890148+0.16418666855j), (-0.0211105132062+0.0459047048958j), (-0.0744047874308-0.010395838657j)], [(-0.108751890148-0.16418666855j), (0.606649542182+0j), (-0.00497137565569-0.0306345815316j), (0.0901180590999+0.0832733570678j)], [(-0.0211105132062-0.0459047048958j), (-0.00497137565569+0.0306345815316j), (0.0765787448398+0j), (-0.0182800951757+0.0679342537664j)], [(-0.0744047874308+0.010395838657j), (0.0901180590999-0.0832733570678j), (-0.0182800951757-0.0679342537664j), (0.17821525801+0j)]], [[(0.286429453556-2.65692879467e-18j), (0.255840322619-0.0423249929902j), (0.251320151504-0.0379769862076j), (0.223994564862-0.0830627336633j)], [(0.255840322619+0.0423249929902j), (0.248421006051-2.30436121699e-18j), (0.234721321192+0.00917392845084j), (0.20457004999-0.0275300601809j)], [(0.251320151504+0.0379769862076j), (0.234721321192-0.00917392845084j), (0.247949098726-1.00870363298e-18j), (0.210079353065-0.0349311018268j)], [(0.223994564862+0.0830627336633j), (0.20457004999+0.0275300601809j), (0.210079353065+0.0349311018268j), (0.217200441668+5.96999364464e-18j)]], [[(0.322750179395+3.10310170627e-18j), (-0.0299241221+0.182081456236j), (-0.0705297896357+0.267203799766j), (0.156665777185+0.0649157704319j)], [(-0.0299241221-0.182081456236j), (0.19810088852+1.90465333384e-18j), (0.203524263032-0.0276069887771j), (0.035461582225-0.155076909618j)], [(-0.0705297896357-0.267203799766j), (0.203524263032+0.0276069887771j), (0.283783388848-4.18538947986e-18j), (0.0371638065473-0.168256418754j)], [(0.156665777185-0.0649157704319j), (0.035461582225+0.155076909618j), (0.0371638065473+0.168256418754j), (0.195365543237-8.22365560242e-19j)]], [[(0.318279216256-2.76063214177e-18j), (0.185041810134+0.134827333749j), (0.169653383543+0.116651534638j), (-0.126427996246-0.134201031961j)], [(0.185041810134-0.134827333749j), (0.254131130099-2.20423618679e-18j), (0.214703963154+0.0296900148183j), (-0.184717288279+0.00638283335375j)], [(0.169653383543-0.116651534638j), (0.214703963154-0.0296900148183j), (0.24772066739+4.79025961788e-18j), (-0.179036502589+8.24366683086e-05j)], [(-0.126427996246+0.134201031961j), (-0.184717288279-0.00638283335375j), (-0.179036502589-8.24366683086e-05j), (0.179868986256+1.74608710689e-19j)]], [[(0.415608512008+1.44193168519e-18j), (-0.0531396941803+0.216053011885j), (0.0181736165982+0.118912428882j), (-0.103474921538-0.0616664088895j)], [(-0.0531396941803-0.216053011885j), (0.24456039755+8.48489325848e-19j), (0.140242767725-0.010297072681j), (-0.0344039536543+0.101527394578j)], [(0.0181736165982-0.118912428882j), (0.140242767725+0.010297072681j), (0.210510176674+7.30353890816e-19j), (-0.0714993741772+0.129631761186j)], [(-0.103474921538+0.0616664088895j), (-0.0344039536543-0.101527394578j), (-0.0714993741772-0.129631761186j), (0.129320913769-3.02077490186e-18j)]], [[(0.0828162341625+5.83632016474e-19j), (-0.00187768684532+0.077310985369j), (-0.0171912442737+0.0252139502043j), (-0.017698409066+0.0351806479045j)], [(-0.00187768684532-0.077310985369j), (0.203671402831+1.43533635324e-18j), (0.040153396804+0.0122545653718j), (-0.114898358913+0.160688968967j)], [(-0.0171912442737-0.0252139502043j), (0.040153396804-0.0122545653718j), (0.0641208321215+3.43459428422e-19j), (0.00695465900773+0.0957846515455j)], [(-0.017698409066-0.0351806479045j), (-0.114898358913-0.160688968967j), (0.00695465900773-0.0957846515455j), (0.649391530886-2.36242779814e-18j)]]]

densityMatrices = Datacube()
densityMatrices.loadtxt("grover - maximum likelihood density matrices-2")

def fromDatacube(cube,row,order = None):
	d = int(sqrt(len(cube.names())))
	densityMatrix = matrix(zeros((d,d),dtype = complex128))
	for i in range(0,d):
		for j in range(0,d):
			if order:
				ii = order[i]
				jj = order[j]
			else:
				ii = i
				jj = j
			densityMatrix[ii,jj] = cube[str(i)+str(j)][row]
	return densityMatrix

matrices = []
for i in range(0,len(densityMatrices)):
	matrices.append(fromDatacube(densityMatrices,i))

rho_initial = matrix([[1.0,0.0],[0.0,0.0]],dtype = complex128)

rho_2 = tensor(rho_initial,rho_initial)

set_printoptions(precision=3,suppress = True)

print "Input:",rho_2

print "Output:",dephase_2(rho_2,1./200.,1./200.,10000.)

print iswap(math.pi/4.,0.2)

print rot_z(math.pi)

#(alpha_1,alpha_2,phi_1,phi_2,beta,d_1,gamma_1,gamma_2,delta,d_2,epsilon_1,epsilon_2,psi_1,psi_2,gamma_1,gamma_2,gammap_1,gammap_2)

step_parameters = []
step_durations = [10.,62.,5.,62.,10.]

T1_1 = 436.
T1_2 = 520.
T_phi_1 = 600.
T_phi_2 = 600.

#Y rotation

import random

random.seed()

def randomize_parameters(n):
	return map(lambda x:random.gauss(0,1.)*math.pi*2.0,range(0,n))

parameters_1 = randomize_parameters(4)

#First swap
parameters_2 = randomize_parameters(4)

#Z rotation
parameters_3_1 = randomize_parameters(2)
parameters_3_2 = randomize_parameters(2)
parameters_3_3 = randomize_parameters(2)
parameters_3_4 = randomize_parameters(2)

#Second swap
parameters_4 = randomize_parameters(4)

#X rotation
parameters_5 = randomize_parameters(4)

def evolve(state,operator,step_duration):
	duration = step_duration
	n = 1
	while duration > 5.0:
		duration /=2.0
		operator = matrix(scipy.linalg.sqrtm(operator))
		n*=2
	for j in range(0,n):
		state = ao(operator,state)
		state = dephase_2(state,1./T_phi_1,1./T_phi_2,duration)
		state = relax_2(state,1./T1_1,1./T1_2,duration)
	return state

def grover_1(state,alpha_1,alpha_2,phi_1,phi_2):
	operator = tensor(rot_phi(alpha_1,phi_1),rot_phi(alpha_2,phi_2))
	return evolve(state,operator,step_durations[0])

def grover_2(state,beta,d_1,betaphi_1,betaphi_2):	
	operator = tensor(rot_z(betaphi_1),rot_z(betaphi_2))*iswap(beta,d_1)
	return evolve(state,operator,step_durations[1])

def grover_3(state,gamma_1,gamma_2):
	operator = tensor(rot_z(gamma_1),rot_z(gamma_2))
	return evolve(state,operator,step_durations[2])

def grover_4(state,delta,d_2,deltaphi_1,deltaphi_2):
	operator = tensor(rot_z(deltaphi_1),rot_z(deltaphi_2))*iswap(delta,d_2)
	return evolve(state,operator,step_durations[3])

def grover_5(state,epsilon_1,epsilon_2,psi_1,psi_2):
	operator = tensor(rot_phi(epsilon_1,psi_1),rot_phi(epsilon_2,psi_2))
	return evolve(state,operator,step_durations[4])

def error_function_1(parameters):
	error = 0
	for state in range(0,4):
		measured_input_state = rho_2
		measured_output_state = matrix(matrices[0+5*state])
		calculated_output_state = grover_1(measured_input_state,*parameters)
		error += 1-abs(stateFidelity(calculated_output_state,measured_output_state))
	return error

def error_function_2(parameters):
	error = 0
	for state in range(0,4):
		measured_input_state = matrix(matrices[0+5*state])
		measured_output_state = matrix(matrices[1+5*state])
		calculated_output_state = grover_2(measured_input_state,*parameters)
		error += 1-abs(stateFidelity(calculated_output_state,measured_output_state))
	return error

def error_function_3(parameters,state):
	error = 0
	measured_input_state = matrix(matrices[1+5*state])
	measured_output_state = matrix(matrices[2+5*state])
	calculated_output_state = grover_3(measured_input_state,*parameters)
	error += 1-abs(stateFidelity(calculated_output_state,measured_output_state))
	return error

def error_function_4(parameters):
	error = 0
	for state in range(0,4):
		measured_input_state = matrix(matrices[2+5*state])
		measured_output_state = matrix(matrices[3+5*state])
		calculated_output_state = grover_4(measured_input_state,*parameters)
		error += 1-abs(stateFidelity(calculated_output_state,measured_output_state))
	return error

def error_function_5(parameters):
	error = 0
	for state in range(0,4):
		measured_input_state = matrix(matrices[3+5*state])
		measured_output_state = matrix(matrices[4+5*state])
		calculated_output_state = grover_5(measured_input_state,*parameters)
		error += 1-abs(stateFidelity(calculated_output_state,measured_output_state))
	return error

oracle_operator = lambda a,b:tensor(rot_z(a*math.pi/2.0),rot_z(b*math.pi/2.0))*iswap(-math.pi/2.0,0)
diffusion_operator = tensor(rot_phi(math.pi/2.,0),rot_phi(math.pi/2.,0))*iswap(-math.pi/2.,0)

from scipy.optimize import fmin

tol = 1e-5

def make_readable(params):
	return map(lambda x:x-360.0 if 360.0-x < x else x,map(lambda x:(x*180.0/math.pi)%360.0,params))

optimized_parameters_1 = fmin(error_function_1,parameters_1,xtol = tol,ftol = tol)
print "Optimized parameters 1:",make_readable(optimized_parameters_1)

optimized_parameters_2 = fmin(error_function_2,parameters_2,xtol = tol,ftol = tol)
print "Optimized parameters 2:",make_readable(optimized_parameters_2)

optimized_parameters_3_1 = fmin(lambda params:error_function_3(params,state = 0),parameters_3_1,xtol = tol,ftol = tol)
print "Optimized parameters 3-1:",make_readable(optimized_parameters_3_1)

optimized_parameters_3_2 = fmin(lambda params:error_function_3(params,state = 1),parameters_3_2,xtol = tol,ftol = tol)
print "Optimized parameters 3-2:",make_readable(optimized_parameters_3_2)

optimized_parameters_3_3 = fmin(lambda params:error_function_3(params,state = 2),parameters_3_3,xtol = tol,ftol = tol)
print "Optimized parameters 3-3:",make_readable(optimized_parameters_3_3)

optimized_parameters_3_4 = fmin(lambda params:error_function_3(params,state = 3),parameters_3_4,xtol = tol,ftol = tol)
print "Optimized parameters 3-4:",make_readable(optimized_parameters_3_4)

optimized_parameters_4 = fmin(error_function_4,parameters_4,xtol = tol,ftol = tol)
print "Optimized parameters 4:",make_readable(optimized_parameters_4)

optimized_parameters_5 = fmin(error_function_5,parameters_5,xtol = tol,ftol = tol)
print "Optimized parameters 5:",make_readable(optimized_parameters_5)


optimized_parameters_3 = (optimized_parameters_3_1,optimized_parameters_3_2,optimized_parameters_3_3,optimized_parameters_3_4)
grover_steps = (grover_1,grover_2,grover_3,grover_4,grover_5)

figure(1,figsize = (20,16))
for state in range(0,4):
	step_parameters = (optimized_parameters_1,optimized_parameters_2,optimized_parameters_3[state],optimized_parameters_4,optimized_parameters_5)
	calculated_matrix = matrix(copy(rho_2))
	for i in range(0,5):
		subplot(4,5,i+1+state*5)
		measured_matrix = matrix(matrices[i+5*state])
		calculated_matrix = grover_steps[i](calculated_matrix,*step_parameters[i])
		if state == 0 and i ==0:
			labels = ["00","01","10","11"]
		else:
			labels = []
		plotDensityMatricesContour([measured_matrix,calculated_matrix],showOutline = [False,True],colors = ['red','black'],labels=labels,annotate = False)
		title("$F$=%.2g %%" % (abs(stateFidelity(measured_matrix,calculated_matrix))*100.))

savefig("grover - simulated density matrices with errors - v4.pdf")
show()

import sys
sys.stdin.readline()

#Optimized parameters 1: [-86.640820735407374, 88.195343671067462, -78.515727923642544, 96.840572880579657]
#Optimized parameters 2: [88.720303371532054, -7.3431185025239643, 160.26477098328292, 159.19317605817503]
#Optimized parameters 3-1: [-92.39344544657115, -98.066825154157868]
#Optimized parameters 3-2: [90.168548505116462, -94.260980331193991]
#Optimized parameters 3-3: [-92.871592140562313, 81.363510506368826]
#Optimized parameters 3-4: [87.306170896838864, 77.526144982079813]
#Optimized parameters 4: [-83.405879395949796, 10.389588676233945, 8.6895247351201874, 4.6363430474926872]
#Optimized parameters 5: [-92.828226992303087, 91.220254404928369, -179.0202560696969, -4.9601230810921493]