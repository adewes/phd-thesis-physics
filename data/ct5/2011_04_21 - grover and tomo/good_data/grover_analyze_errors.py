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
matrices = [[[(0.277717003178-1.4782827649e-18j), (0.248720259174-0.0479223051138j), (0.243234413481-0.0252981556514j), (0.217361643952-0.0832260226772j)], [(0.248720259174+0.0479223051138j), (0.242169702828-1.28906510503e-18j), (0.230292303658+0.0181348863685j), (0.205449342684-0.0225580715578j)], [(0.243234413481+0.0252981556514j), (0.230292303658-0.0181348863685j), (0.256402436182-2.85526081365e-18j), (0.206132601145-0.0553914249732j)], [(0.217361643952+0.0832260226772j), (0.205449342684+0.0225580715578j), (0.206132601145+0.0553914249732j), (0.223710857812+5.62260868359e-18j)]], [[(0.323017477798-8.4051900283e-19j), (-0.0226700791735+0.206639192754j), (-0.0474527328796+0.271651484849j), (0.167236803214+0.022331014302j)], [(-0.0226700791735-0.206639192754j), (0.197899436852-5.14951198484e-19j), (0.206435121312-0.00291658347138j), (0.00180578839165-0.164862172013j)], [(-0.0474527328796-0.271651484849j), (0.206435121312+0.00291658347138j), (0.275682370651+2.75209793153e-18j), (-0.00365998383998-0.184097914936j)], [(0.167236803214-0.022331014302j), (0.00180578839165+0.164862172013j), (-0.00365998383998+0.184097914936j), (0.2034007147-1.39662773022e-18j)]], [[(0.349040759194+0j), (-0.226302910115-0.0657672681072j), (-0.184235058152-0.059381422711j), (-0.203539472688-0.00167881672382j)], [(-0.226302910115+0.0657672681072j), (0.239147130162+0j), (0.16087704702+0.0422993881323j), (0.167979356386+0.000204237509748j)], [(-0.184235058152+0.059381422711j), (0.16087704702-0.0422993881323j), (0.224097584642+0j), (0.163971547364+0.0129738288716j)], [(-0.203539472688+0.00167881672382j), (0.167979356386-0.000204237509748j), (0.163971547364-0.0129738288716j), (0.187714526002+0j)]], [[(0.391409720995+8.48734539669e-20j), (0.00410950509939-0.21081868786j), (0.0187288947002-0.159200553913j), (-0.141888557981-0.00657227461839j)], [(0.00410950509939+0.21081868786j), (0.248280609489+5.38372752389e-20j), (0.162785143225+0.0535921836272j), (0.0154053851236-0.131991195984j)], [(0.0187288947002+0.159200553913j), (0.162785143225-0.0535921836272j), (0.219777380926+4.76566227727e-20j), (-0.00238754118138-0.101971370332j)], [(-0.141888557981+0.00657227461839j), (0.0154053851236+0.131991195984j), (-0.00238754118138+0.101971370332j), (0.140532288589-1.86367351979e-19j)]], [[(0.676314789692-8.06588160695e-19j), (-0.0547649822398+0.147104536213j), (-0.0514328790472+0.0803112341581j), (-0.00425507192827-0.0114732988693j)], [(-0.0547649822398-0.147104536213j), (0.120596165334-1.43825686893e-19j), (0.0207806694769+0.0213122855972j), (-0.0370840018113+0.0410357855819j)], [(-0.0514328790472-0.0803112341581j), (0.0207806694769-0.0213122855972j), (0.110926974842+1.92966657923e-19j), (-0.000978019772056+0.0704594745651j)], [(-0.00425507192827+0.0114732988693j), (-0.0370840018113-0.0410357855819j), (-0.000978019772056-0.0704594745651j), (0.0921620701321+7.57447189665e-19j)]], [[(0.288621006504-2.08144598898e-18j), (0.254415619066-0.0459844520245j), (0.247067892548-0.0292612227046j), (0.219947625382-0.0844594737492j)], [(0.254415619066+0.0459844520245j), (0.246321887874-1.77639774639e-18j), (0.22487210382+0.0253618041908j), (0.204736187742-0.0220616529575j)], [(0.247067892548+0.0292612227046j), (0.22487210382-0.0253618041908j), (0.246619821693-9.30111925028e-19j), (0.203239807632-0.0532386620155j)], [(0.219947625382+0.0844594737492j), (0.204736187742+0.0220616529575j), (0.203239807632+0.0532386620155j), (0.218437283929+4.7879556604e-18j)]], [[(0.324161269994+0j), (-0.011618810831+0.209230619758j), (-0.0119539455745+0.264599938364j), (0.173439641448+0.02392573071j)], [(-0.011618810831-0.209230619758j), (0.202578727369+0j), (0.197090127894-0.0255650500769j), (-0.00156564608673-0.160822564848j)], [(-0.0119539455745-0.264599938364j), (0.197090127894+0.0255650500769j), (0.2759344467+0j), (-0.00673486229983-0.184396129846j)], [(0.173439641448-0.02392573071j), (-0.00156564608673+0.160822564848j), (-0.00673486229983+0.184396129846j), (0.197325555938+0j)]], [[(0.290751862136-1.00874816186e-18j), (0.197576778126+0.0685752309767j), (-0.206470788038-0.0677680997736j), (0.158641990977-0.0189745881923j)], [(0.197576778126-0.0685752309767j), (0.257372904446-8.92941638847e-19j), (-0.186806702562-0.0256885679343j), (0.154398372981-0.044410576234j)], [(-0.206470788038+0.0677680997736j), (-0.186806702562+0.0256885679343j), (0.298675433076+2.43320838105e-18j), (-0.184423711272+0.0463924645799j)], [(0.158641990977+0.0189745881923j), (0.154398372981+0.044410576234j), (-0.184423711272-0.0463924645799j), (0.153199800342-5.31518580337e-19j)]], [[(0.432799127213+3.00314722544e-18j), (-0.0446689339182-0.130531979597j), (0.0336712656174+0.184871490353j), (0.122267071991-0.0508687033958j)], [(-0.0446689339182+0.130531979597j), (0.168235408194+1.16736764834e-18j), (-0.122523460576-0.0648856430539j), (-0.000786952233997+0.0771348968226j)], [(0.0336712656174-0.184871490353j), (-0.122523460576+0.0648856430539j), (0.273083501018-1.57454951148e-18j), (-0.0589975349438-0.144785106247j)], [(0.122267071991+0.0508687033958j), (-0.000786952233997-0.0771348968226j), (-0.0589975349438+0.144785106247j), (0.125881963575-2.59596536229e-18j)]], [[(0.108876714263+9.44354961098e-20j), (-0.0182342255286+0.0658362076538j), (-0.0906862960555+0.0313177706588j), (-0.0352022402927-0.0240616388672j)], [(-0.0182342255286-0.0658362076538j), (0.0986981123492+8.56069662634e-20j), (0.0533583927598+0.0352137365698j), (-0.0399977354455+0.0611146313827j)], [(-0.0906862960555-0.0313177706588j), (0.0533583927598-0.0352137365698j), (0.635691364224+5.51374366498e-19j), (-0.0123831470486+0.218829182791j)], [(-0.0352022402927+0.0240616388672j), (-0.0399977354455-0.0611146313827j), (-0.0123831470486-0.218829182791j), (0.156733809163-7.31416828871e-19j)]], [[(0.289342152533-3.07315677349e-19j), (0.248778716951-0.0492608575249j), (0.253824349633-0.0272288707884j), (0.224599880627-0.089389795834j)], [(0.248778716951+0.0492608575249j), (0.238178673521-2.52973995466e-19j), (0.231979774805+0.0174071622451j), (0.205567308633-0.0222416169766j)], [(0.253824349633+0.0272288707884j), (0.231979774805-0.0174071622451j), (0.246650718678+1.22499370557e-18j), (0.209056122341-0.0416574596142j)], [(0.224599880627+0.089389795834j), (0.205567308633+0.0222416169766j), (0.209056122341+0.0416574596142j), (0.225828455269-6.64704032757e-19j)]], [[(0.329448575601-1.14300435644e-18j), (-0.0549773184933+0.173734486895j), (-0.0867316838417+0.273638898616j), (0.154840482357+0.0972360489541j)], [(-0.0549773184933-0.173734486895j), (0.193688406755-6.71991652445e-19j), (0.203360852198-0.0318492400956j), (0.0449070710309-0.152030991447j)], [(-0.0867316838417-0.273638898616j), (0.203360852198+0.0318492400956j), (0.284379591804+2.48280704397e-18j), (0.0586605745536-0.169619181118j)], [(0.154840482357-0.0972360489541j), (0.0449070710309+0.152030991447j), (0.0586605745536+0.169619181118j), (0.192483425841-6.67811035085e-19j)]], [[(0.354387223498+0j), (-0.204209393526-0.120267540146j), (0.159301084887+0.110847991964j), (0.126344970011+0.132771027517j)], [(-0.204209393526+0.120267540146j), (0.23058360085+0j), (-0.172597268561-0.00293859583j), (-0.18978793476-0.00767300632125j)], [(0.159301084887-0.110847991964j), (-0.172597268561+0.00293859583j), (0.208817689959-1.73472347598e-18j), (0.16441917258+0.0520773830112j)], [(0.126344970011-0.132771027517j), (-0.18978793476+0.00767300632125j), (0.16441917258-0.0520773830112j), (0.206211485694+1.73472347598e-18j)]], [[(0.396024073839-5.15244193456e-19j), (-0.0784850026609+0.15229582638j), (0.0565243010776-0.205843339809j), (0.098826405083+0.0719783649678j)], [(-0.0784850026609-0.15229582638j), (0.193966649387-2.52358875186e-19j), (-0.141781296753+0.0158636911273j), (0.0141900110389-0.0988986574604j)], [(0.0565243010776+0.205843339809j), (-0.141781296753-0.0158636911273j), (0.271073317889+9.48364670793e-19j), (-0.0537316362809+0.158492240962j)], [(0.098826405083-0.0719783649678j), (0.0141900110389+0.0988986574604j), (-0.0537316362809-0.158492240962j), (0.138935958886-1.80761602152e-19j)]], [[(0.138556454969+0j), (-0.108751890148+0.16418666855j), (-0.0211105132062+0.0459047048958j), (-0.0744047874308-0.010395838657j)], [(-0.108751890148-0.16418666855j), (0.606649542182+0j), (-0.00497137565569-0.0306345815316j), (0.0901180590999+0.0832733570678j)], [(-0.0211105132062-0.0459047048958j), (-0.00497137565569+0.0306345815316j), (0.0765787448398+0j), (-0.0182800951757+0.0679342537664j)], [(-0.0744047874308+0.010395838657j), (0.0901180590999-0.0832733570678j), (-0.0182800951757-0.0679342537664j), (0.17821525801+0j)]], [[(0.286429453556-2.65692879467e-18j), (0.255840322619-0.0423249929902j), (0.251320151504-0.0379769862076j), (0.223994564862-0.0830627336633j)], [(0.255840322619+0.0423249929902j), (0.248421006051-2.30436121699e-18j), (0.234721321192+0.00917392845084j), (0.20457004999-0.0275300601809j)], [(0.251320151504+0.0379769862076j), (0.234721321192-0.00917392845084j), (0.247949098726-1.00870363298e-18j), (0.210079353065-0.0349311018268j)], [(0.223994564862+0.0830627336633j), (0.20457004999+0.0275300601809j), (0.210079353065+0.0349311018268j), (0.217200441668+5.96999364464e-18j)]], [[(0.322750179395+3.10310170627e-18j), (-0.0299241221+0.182081456236j), (-0.0705297896357+0.267203799766j), (0.156665777185+0.0649157704319j)], [(-0.0299241221-0.182081456236j), (0.19810088852+1.90465333384e-18j), (0.203524263032-0.0276069887771j), (0.035461582225-0.155076909618j)], [(-0.0705297896357-0.267203799766j), (0.203524263032+0.0276069887771j), (0.283783388848-4.18538947986e-18j), (0.0371638065473-0.168256418754j)], [(0.156665777185-0.0649157704319j), (0.035461582225+0.155076909618j), (0.0371638065473+0.168256418754j), (0.195365543237-8.22365560242e-19j)]], [[(0.318279216256-2.76063214177e-18j), (0.185041810134+0.134827333749j), (0.169653383543+0.116651534638j), (-0.126427996246-0.134201031961j)], [(0.185041810134-0.134827333749j), (0.254131130099-2.20423618679e-18j), (0.214703963154+0.0296900148183j), (-0.184717288279+0.00638283335375j)], [(0.169653383543-0.116651534638j), (0.214703963154-0.0296900148183j), (0.24772066739+4.79025961788e-18j), (-0.179036502589+8.24366683086e-05j)], [(-0.126427996246+0.134201031961j), (-0.184717288279-0.00638283335375j), (-0.179036502589-8.24366683086e-05j), (0.179868986256+1.74608710689e-19j)]], [[(0.415608512008+1.44193168519e-18j), (-0.0531396941803+0.216053011885j), (0.0181736165982+0.118912428882j), (-0.103474921538-0.0616664088895j)], [(-0.0531396941803-0.216053011885j), (0.24456039755+8.48489325848e-19j), (0.140242767725-0.010297072681j), (-0.0344039536543+0.101527394578j)], [(0.0181736165982-0.118912428882j), (0.140242767725+0.010297072681j), (0.210510176674+7.30353890816e-19j), (-0.0714993741772+0.129631761186j)], [(-0.103474921538+0.0616664088895j), (-0.0344039536543-0.101527394578j), (-0.0714993741772-0.129631761186j), (0.129320913769-3.02077490186e-18j)]], [[(0.0828162341625+5.83632016474e-19j), (-0.00187768684532+0.077310985369j), (-0.0171912442737+0.0252139502043j), (-0.017698409066+0.0351806479045j)], [(-0.00187768684532-0.077310985369j), (0.203671402831+1.43533635324e-18j), (0.040153396804+0.0122545653718j), (-0.114898358913+0.160688968967j)], [(-0.0171912442737-0.0252139502043j), (0.040153396804-0.0122545653718j), (0.0641208321215+3.43459428422e-19j), (0.00695465900773+0.0957846515455j)], [(-0.017698409066-0.0351806479045j), (-0.114898358913-0.160688968967j), (0.00695465900773-0.0957846515455j), (0.649391530886-2.36242779814e-18j)]]]

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

decoherence_parameters = (450.,500.,800.,800.)

step_parameters.append( (math.pi/2,math.pi/2,math.pi/2,math.pi/2))
step_parameters.append( (-math.pi/2,0))
step_parameters.append( (math.pi/2,-math.pi/2))
step_parameters.append( (-math.pi/2,0))
step_parameters.append( (math.pi/2,math.pi/2,0,0))

print step_parameters



def concatenate(a,b):
	l = list(a)
	l+= list(b)
	return l

parameters = reduce(concatenate,step_parameters)

print "Parameter:",parameters

def grover(rho,step,parameters,decoherence_parameters):
	(alpha_1,alpha_2,phi_1,phi_2,beta,d_1,gamma_1,gamma_2,delta,d_2,epsilon_1,epsilon_2,psi_1,psi_2,T1_1,T1_2,T_phi_1,T_phi_2) = list(parameters)+list(decoherence_parameters)
	step1 = tensor(rot_phi(alpha_1,phi_1),rot_phi(alpha_2,phi_2))
	step2 = iswap(beta,d_1)
	step3 = tensor(rot_z(gamma_1),rot_z(gamma_2))
	step4 = iswap(delta,d_2)
	step5 = tensor(rot_phi(epsilon_1,psi_1),rot_phi(epsilon_2,psi_2))

	steps = (step1,step2,step3,step4,step5)

	state = rho
	
	for i in range(0,step+1):
		state = ao(steps[i],state)
		state = dephase_2(state,1./T_phi_1,1./T_phi_2,step_durations[step])
		state = relax_2(state,1./T1_1,1./T1_2,step_durations[step])
	return state

oracle_operator = lambda a,b:tensor(rot_z(a*math.pi/2.0),rot_z(b*math.pi/2.0))*iswap(-math.pi/2.0,0)
diffusion_operator = tensor(rot_phi(math.pi/2.,0),rot_phi(math.pi/2.,0))*iswap(-math.pi/2.,0)

#Oracle operator fidelities:
#0.945,0.936,0.885,0.877 = 0.911 avg fidelity

#diffusion operator fidelities:
#0.923,0.934,0.943,0.917 = 0.929 avg fidelity

step = 4

def error_function(state,parameters,decoherence_parameters,verbose = False):
	full_error = 0
	for step in range(0,5):
		measured_state = matrix(matrices[step+5*state])
		calculated_state = grover(rho_2,step,parameters,decoherence_parameters)
		fidelity = abs(stateFidelity(measured_state,calculated_state))
		if verbose:
			print "Fidelity at step %d:%g" %(step,fidelity)
		full_error+=1-fidelity
	return full_error

state = 3

initial_phases = ((-math.pi/2.0,-math.pi/2.0),(math.pi/2.0,-math.pi/2.0),(-math.pi/2.0,math.pi/2.0),(math.pi/2.0,math.pi/2.0))

(parameters[6],parameters[7]) = initial_phases[state]

print error_function(state,parameters,decoherence_parameters,verbose = True)

from scipy.optimize import fmin

print "Optimizing parameters..."

optimized_parameter_sets = []


for state in range(0,4):

	(parameters[6],parameters[7]) = initial_phases[state]
	
	optimized_parameters = fmin(lambda params,state = state:error_function(state,params,decoherence_parameters),list(parameters),xtol = 1e-5,ftol = 1e-5)
	optimized_parameter_sets.append(list(optimized_parameters))

	print error_function(state,optimized_parameters,decoherence_parameters,verbose = True)

	print "Optimized parameters:",optimized_parameters

calculated_matrices = []

figure(1,figsize = (20,16))
for state in range(0,4):
	optimized_parameters = optimized_parameter_sets[state]
	for i in range(0,5):
		subplot(4,5,i+1+state*5)
		measured_matrix = matrix(matrices[i+5*state])
		calculated_matrix = grover(rho_2,i,optimized_parameters,decoherence_parameters)
		calculated_matrices.append(calculated_matrix.tolist())
		if state == 0 and i ==0:
			labels = ["00","01","10","11"]
		else:
			labels = []
		plotDensityMatricesContour([measured_matrix,calculated_matrix],showOutline = [False,True],colors = ['red','black'],labels=labels)
		title("$F$=%.2g %%" % (abs(stateFidelity(measured_matrix,calculated_matrix))*100.))

savefig("grover - simulated density matrices with errors.pdf")
show()

print optimized_parameter_sets
print calculated_matrices

import sys

sys.stdin.readline()

resulting_matrices = [[[(0.25937978014623503+0j), (0.23865066849742045-0.025362465637224496j), (0.2603504464246408-0.01416983022246062j), (0.2381582180997796-0.03849478436806796j)], [(0.23865066849742045+0.025362465637224496j), (0.22893319890193103+0j), (0.2409293040487294+0.01241997272948414j), (0.22978992619214766-0.012506543720934132j)], [(0.2603504464246408+0.01416983022246062j), (0.2409293040487294-0.01241997272948414j), (0.27179549324466606+0j), (0.2500741427140392-0.026576488937896058j)], [(0.2381582180997796+0.03849478436806796j), (0.22978992619214766+0.012506543720934132j), (0.2500741427140392+0.026576488937896058j), (0.23989152770716768+0j)]], [[(0.37769854876898157-4.0460745558568543e-19j), (-0.021102757412583495+0.19778259777695206j), (-0.010128131959231883+0.21342915946057076j), (0.16235228420234415-0.026241866528469413j)], [(-0.021102757412583495-0.19778259777695206j), (0.23418553648652676-3.0648394963679284e-18j), (0.1647709557496964-0.007390288163983101j), (-0.0355259835256283-0.15043176968473126j)], [(-0.010128131959231883-0.21342915946057076j), (0.1647709557496964+0.0073902881639831015j), (0.2398728108663635+0j), (-0.02945563436221199-0.15543285029805815j)], [(0.16235228420234415+0.026241866528469413j), (-0.0355259835256283+0.1504317696847313j), (-0.02945563436221199+0.15543285029805815j), (0.14824310387812795+0j)]], [[(0.26465244768815355+3.6154005802767065e-18j), (-0.2354212285687319-0.03195644660299211j), (-0.24323874207032153-0.025199326659602228j), (-0.23711097444684628+0.00747492153468249j)], [(-0.23542122856873188+0.03195644660299211j), (0.24498639871375708+6.655167919842516e-18j), (0.23799877764418798-0.007157621393030421j), (0.2308018883967278-0.037303977244391544j)], [(-0.24323874207032148+0.025199326659602225j), (0.23799877764418795+0.007157621393030425j), (0.2554809194814129+7.076666259648849e-18j), (0.2371854923848766-0.031051656643495743j)], [(-0.23711097444684628-0.00747492153468249j), (0.23080188839672777+0.03730397724439155j), (0.2371854923848766+0.031051656643495743j), (0.23488023411667622+0j)]], [[(0.49454093193572674-6.052128440230954e-19j), (0.005216497181347717-0.1818919514476691j), (0.006248956210033444-0.148826213648248j), (-0.10835245537770449+0.0034158102716586388j)], [(0.005216497181347709+0.18189195144766906j), (0.22592507458753036+0j), (0.10781163309037756+0.0016059792783083354j), (-0.0010098613395276089-0.10481549800404637j)], [(0.006248956210033458+0.14882621364824802j), (0.10781163309037756-0.0016059792783083328j), (0.1917132295040149-1.511451191189589e-18j), (-0.001841579294266269-0.0901587461282892j)], [(-0.10835245537770449-0.0034158102716586388j), (-0.0010098613395276058+0.10481549800404637j), (-0.0018415792942662662+0.09015874612828921j), (0.08782076397272778+0j)]], [[(0.8487192031592168+6.0075507739787885e-18j), (-0.00010239211437634445+0.2039548249506668j), (-0.01977238890997832+0.12333301911994338j), (-0.029242578056173276-0.003106811109850126j)], [(-0.00010239211437634222-0.2039548249506669j), (0.08002092779452177-4.582595565148111e-18j), (0.02779992359991636+0.004815321437397965j), (-0.00017551563962413385+0.01759088637429991j)], [(-0.019772388909978306-0.12333301911994335j), (0.027799923599916315-0.004815321437397957j), (0.043479890225474355+1.1653656337267672e-18j), (0.00155431059812606+0.016646967631667946j)], [(-0.029242578056173255+0.003106811109850127j), (-0.00017551563962412784-0.017590886374299872j), (0.0015543105981260495-0.01664696763166792j), (0.02777997882078661-5.300826273771204e-18j)]], [[(0.260695122287979+0j), (0.248497980867707-0.034368530558021894j), (0.25070568648714003-0.015900916813116804j), (0.23687963624612113-0.04820854206556647j)], [(0.248497980867707+0.034368530558021894j), (0.24925317385766507+0j), (0.24107220525620393+0.01789462067473957j), (0.23970217590820608-0.015203023164115526j)], [(0.25070568648714003+0.015900916813116804j), (0.24107220525620393-0.01789462067473957j), (0.25052361156876274+0j), (0.23880236457110696-0.0330275776705779j)], [(0.23687963624612113+0.04820854206556647j), (0.23970217590820608+0.015203023164115526j), (0.23880236457110696+0.0330275776705779j), (0.2395280922855931+0j)]], [[(0.37869521077543256+1.7023040503202444e-18j), (-0.03548100789675857+0.19540959290487717j), (-0.017033340839897916+0.21596206940129217j), (0.1614806758818866-0.03286372809159322j)], [(-0.03548100789675857-0.19540959290487717j), (0.22723300411620537+6.129678992735857e-18j), (0.16376941317340055-0.014614755003215432j), (-0.04972654267575867-0.14351932779815893j)], [(-0.017033340839897916-0.21596206940129217j), (0.16376941317340055+0.014614755003215435j), (0.24605326938250627+6.045804764758356e-18j), (-0.039247505210926244-0.15541615075236398j)], [(0.1614806758818866+0.03286372809159322j), (-0.04972654267575867+0.14351932779815893j), (-0.039247505210926244+0.15541615075236398j), (0.1480185157258559+0j)]], [[(0.26599733936938297-1.6197153614233814e-18j), (0.2275499734097011+0.05667554761694238j), (-0.24872018398643833-0.004099623082197691j), (0.2355453105816888-0.03198395808196304j)], [(0.22754997340970112-0.05667554761694238j), (0.23696720390451734+0j), (-0.2313266803856393+0.05310873076839603j), (0.2141173476395285-0.0831003074155781j)], [(-0.24872018398643833+0.004099623082197694j), (-0.23132668038563925-0.053108730768396034j), (0.2625110659262828+1.0293332741307418e-17j), (-0.23982617927384828+0.0349560318904905j)], [(0.2355453105816888+0.03198395808196304j), (0.21411734763952853+0.0831003074155781j), (-0.23982617927384828-0.03495603189049052j), (0.23452439079981702+0j)]], [[(0.4963610868893657+4.269281971706343e-18j), (-0.0228387333366736-0.1355613985389895j), (-0.03013678990342947+0.1895312413497186j), (0.10763699492935655-0.014615689547744448j)], [(-0.02283873333667359+0.13556139853898952j), (0.15659365691952704+9.270422313946214e-18j), (-0.09163846086327025-0.030462380255697724j), (-0.007386620865395482+0.07192079161819495j)], [(-0.030136789903429474-0.18953124134971858j), (-0.09163846086327027+0.030462380255697724j), (0.25935754058687555-2.955068118452481e-18j), (-0.024963773089359934-0.11457104864542375j)], [(0.10763699492935655+0.014615689547744448j), (-0.007386620865395488-0.07192079161819495j), (-0.024963773089359934+0.11457104864542375j), (0.08768771560423187+5.138341580696837e-19j)]], [[(0.05599876683697432+6.046523897543768e-20j), (0.002751261333279369+0.024169341434578953j), (-0.04401979722352444+0.06056210705039335j), (-0.021871707049578852-0.015667396121134547j)], [(0.0027512613332793734-0.024169341434578925j), (0.034705191585073424-4.555723384917401e-18j), (0.0419750261414259+0.02042066812042773j), (-0.008777270176776354+0.027187453054351822j)], [(-0.04401979722352447-0.06056210705039346j), (0.041975026141425925-0.020420668120427733j), (0.7664181316724232+6.4168528744252e-18j), (0.023351979401869498+0.29863506171314846j)], [(-0.021871707049578883+0.01566739612113455j), (-0.008777270176776358-0.027187453054351895j), (0.02335197940186949-0.2986350617131483j), (0.14287790990552882-1.829304753301435e-17j)]], [[(0.2662089698940286+0j), (0.24371232176309476-0.004378096655455787j), (0.2632559907037722+0.011336398323105401j), (0.24119533081700115+0.006048856219861386j)], [(0.24371232176309476+0.004378096655455787j), (0.23001089189176807+0j), (0.2408224519646991+0.014707919608203945j), (0.2274594475224852+0.009794918218480008j)], [(0.2632559907037722-0.011336398323105401j), (0.2408224519646991-0.014707919608203945j), (0.27026486034725883+0j), (0.24742545915124142-0.004444800194541081j)], [(0.24119533081700115-0.006048856219861386j), (0.2274594475224852-0.009794918218480008j), (0.24742545915124142+0.004444800194541081j), (0.23351527786694445+0j)]], [[(0.38425707823272487+4.0460745558568543e-19j), (-0.03749901277951565+0.19107875667782345j), (-0.0259535951942417+0.22087221803247475j), (0.16442268173451885+0.004123500889205561j)], [(-0.03749901277951565-0.19107875667782345j), (0.22345052177460542+3.0648394963679284e-18j), (0.1640664068093367-0.010159257096153895j), (-0.020138767565598074-0.14692118813761598j)], [(-0.0259535951942417-0.22087221803247475j), (0.1640664068093367+0.01015925709615389j), (0.24798955643324266+0j), (-0.01192595510084146-0.15953568338840296j)], [(0.16442268173451885-0.004123500889205561j), (-0.020138767565598074+0.14692118813761598j), (-0.01192595510084146+0.15953568338840296j), (0.144302843559427+0j)]], [[(0.2715057214507684+1.3895048594799647e-17j), (-0.2131980190551632-0.0964369781895908j), (0.22410473245301119+0.1202489867563425j), (0.18569147162184008+0.14766992571334714j)], [(-0.2131980190551632+0.0964369781895908j), (0.23202949383070962+1.7174626889916169e-18j), (-0.2368144046805617-0.01651053603581301j), (-0.2172129433818081-0.056117772136178024j)], [(0.22410473245301113-0.1202489867563425j), (-0.2368144046805617+0.016510536035813015j), (0.2678276016573471+0j), (0.237882580066391+0.04407779765311356j)], [(0.18569147162184008-0.14766992571334714j), (-0.2172129433818081+0.05611777213617803j), (0.23788258006639096-0.04407779765311356j), (0.22863718306117498+0j)]], [[(0.5011654880762427+6.668357512567569e-19j), (-0.0572531749657254+0.13856526809033176j), (0.06564578341009439-0.17171309882538846j), (0.08485531696651213+0.0674806346429622j)], [(-0.05725317496572538-0.13856526809033176j), (0.16730241039309868-6.072305987394306e-19j), (-0.10154399157250377+0.0031522558026454697j), (0.02474829514162057-0.07406951541069481j)], [(0.06564578341009442+0.17171309882538846j), (-0.10154399157250374-0.0031522558026454727j), (0.2460455889489718+2.4802282709656007e-18j), (-0.03876884797796418+0.10453150823043172j)], [(0.08485531696651213-0.0674806346429622j), (0.02474829514162057+0.07406951541069484j), (-0.03876884797796418-0.10453150823043164j), (0.08548651258168687-4.110673264557469e-18j)]], [[(0.120380798922731+9.066806614974543e-20j), (-0.1495056574822667+0.197457080149577j), (0.02360708303458855+0.030558789504202717j), (-0.06870935816270304+0.016488675057443065j)], [(-0.14950565748226669-0.19745708014957705j), (0.7422824552508436-7.100449227013603e-18j), (0.012583559790146538-0.07297831973282198j), (0.1681599338068284+0.1391385269467948j)], [(0.023607083034588527-0.03055878950420266j), (0.012583559790146519+0.07297831973282201j), (0.039313727348871785+1.014942036327724e-17j), (-0.01382216009663874+0.03286847075517083j)], [(-0.06870935816270304-0.01648867505744305j), (0.1681599338068284-0.13913852694679477j), (-0.013822160096638742-0.032868470755170895j), (0.09802301847755326-1.3304034569464981e-17j)]], [[(0.26793220077804497+0j), (0.23342175590506242-0.008853693271431718j), (0.27506989470618237-0.004500503693068847j), (0.23949137712203789-0.013010380761641361j)], [(0.23342175590506242+0.008853693271431718j), (0.2095203561337067+0j), (0.23978881116803663+0.005168729243512746j), (0.21510196285904246-0.0035193497975033777j)], [(0.27506989470618237+0.004500503693068847j), (0.23978881116803663-0.005168729243512746j), (0.2932381121658803+0j), (0.25546819248033514-0.00968991518403239j)], [(0.23949137712203789+0.013010380761641361j), (0.21510196285904246+0.0035193497975033777j), (0.25546819248033514+0.00968991518403239j), (0.22930933092236797+0j)]], [[(0.3866468529797235-4.0460745558568543e-19j), (-0.03783401333574794+0.18257693177496667j), (-0.035520342386830286+0.22981117310447463j), (0.16326109773897346-0.008869167110201281j)], [(-0.03783401333574794-0.18257693177496667j), (0.21407921438386524-3.0648394963679284e-18j), (0.1643995143183383-0.002520153312873698j), (-0.029045001362810765-0.13951128610690505j)], [(-0.035520342386830286-0.22981117310447463j), (0.1643995143183383+0.0025201533128737037j), (0.25757019141198567+0j), (-0.03047889459281798-0.1603216495399503j)], [(0.16326109773897346+0.008869167110201281j), (-0.029045001362810765+0.13951128610690508j), (-0.03047889459281798+0.1603216495399503j), (0.1417037412244256+0j)]], [[(0.27326253282791185-1.37478075706766e-17j), (0.19789698554769403+0.11188460460385134j), (0.2422498084136267+0.10320639825377956j), (-0.19920350873160966-0.12626160132982084j)], [(0.197896985547694-0.11188460460385134j), (0.21886804306132862+5.304206419899416e-18j), (0.23584666337428586-0.025449346344186184j), (-0.2152756897287077-0.012790494182283023j)], [(0.24224980841362673-0.10320639825377957j), (0.2358466633742859+0.02544934634418619j), (0.28335032647121866+6.998782323606465e-18j), (-0.2434897490524349-0.041048732864809j)], [(-0.19920350873160966+0.12626160132982084j), (-0.2152756897287077+0.012790494182283018j), (-0.24348974905243498+0.04104873286480902j), (0.2245190976395409+1.3587883159008368e-17j)]], [[(0.5031027001942314+2.211754290877808e-18j), (-0.034267589201774765+0.1739578395448443j), (-0.04103867264324612+0.15785636809293396j), (-0.09102990420952647-0.0576976858870519j)], [(-0.03426758920177477-0.1739578395448443j), (0.20073720670029657+3.0648394963679284e-18j), (0.10857407608954425+0.009615882343621648j), (-0.04215031820568642+0.08290521444206715j)], [(-0.041038672643246135-0.15785636809293396j), (0.10857407608954424-0.00961588234362163j), (0.21221331590932307+1.2091609529516712e-17j), (-0.03665049985331573+0.09117261107339908j)], [(-0.09102990420952647+0.0576976858870519j), (-0.04215031820568643-0.08290521444206715j), (-0.03665049985331575-0.09117261107339909j), (0.083946777196149+0j)]], [[(0.03416394603388947+3.7604756488423154e-18j), (0.004348023820678886+0.023994989441132788j), (0.00033505814326264096+0.01733787661853159j), (-0.0379907430813344+0.018666290126389977j)], [(0.004348023820678896-0.023994989441132715j), (0.13445308233664569+7.801158737773175e-18j), (0.04285420571959874-0.006437751555381661j), (-0.11087185193612392+0.22720162697780824j)], [(0.0003350581432626301-0.01733787661853161j), (0.04285420571959879+0.006437751555381666j), (0.06188725345843575+6.072476992327316e-18j), (-0.07668885915430933+0.11620864004097851j)], [(-0.03799074308133441-0.01866629012638998j), (-0.11087185193612392-0.2272016269778083j), (-0.07668885915430931-0.11620864004097842j), (0.7694957181710291+6.6520172847324904e-18j)]]]
resulting_parameters = [
	[1.5273739111910305, 1.6171832148650473, 1.6766733573338262, 1.6251686699069765,
	 -1.6973632392540172, 0.062732949030268839, -1.6286919455472204, -1.6416355270731593,
	 -1.4396939582245771, -0.060674104636515333, 2.0772822078946001, 1.7336993503730873,
	 0.011504536624492686, -0.029348351047189112],
	[1.5681069289515439, 1.572923615278468, 1.7082295345446754, 1.634136121329361, -1.7577998162401753, 0.044632918793367948, 1.4670640281593039, -1.5328756072252143, -1.6918588930608123, -0.31087849580774041, 2.0600939529956426, 1.2367967475252204, 0.15741409611061435, 0.034450620939837751], [1.5165497646282251, 1.6010020580100832, 1.5887585937805264, 1.5277606533026855, -1.6836298796432803, 0.087385367390623747, -1.8293071052081231, 1.182546644562505, -1.7008594024086903, -0.20877953565691343, 1.304948975092679, 2.128634441252534, 0.062018521786386019, 0.091444011108024553], [1.4659938509888508, 1.6394293839699707, 1.6087081786745081, 1.5871561766386755, -1.7371938924632757, 0.15857367608609099, 1.2150105656399017, 1.3073850108360321, -1.2686640722625178, 0.1270306677344612, 1.3659033849032145, 1.0094769537155153, -0.12199623295335274, -0.15453780858767985]]

def map_parameters(params):
	angles = params[:5]+params[6:9]+params[10:]
	deltas = (params[5],params[9])
	print len(angles),len(deltas)
	deviations = []
	for angle in angles:
		if abs(abs(angle)-math.pi/2.0) < abs(angle):
			if angle < 0:
				deviations.append((angle+math.pi/2.0)*180./math.pi)
			else:
				deviations.append((angle-math.pi/2.0)*180./math.pi)
		else:
			deviations.append(angle*180.0/math.pi)
	return list(deltas)+deviations