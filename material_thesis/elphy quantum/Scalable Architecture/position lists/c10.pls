
[HEADER]
FORMAT=IXYZRTUVWATC,Options,65,Type,17,Size-U,11,Size-V,11,Points-U,11,Points-V,11,Dir,5,Avg,5,Pos1,12,Pos2,12,Pos3,12,Link,9,File,222,Layer,65,Area,49,DoseFactor,11,Dwelltime,11,Stepsize,11,SplDwell,11,SplStep,11,CurveStep,11,CurveDwell,11,DotDwell,11,FBMSArea,11,FBMSLines,11,SplDot,5,Time,17,Timestamp,18,Method,17,Dot,16
WAFERLAYOUT=DEFAULT.wlo
LotID=
WaferID=
Slot=
MinimizeWin=FALSE

[COLUMNS]
No.=W:25,!VISIBLE,!SHOWDIM
ID=W:25,VISIBLE,!SHOWDIM
X=W:50,!VISIBLE,SHOWDIM
Y=W:50,!VISIBLE,SHOWDIM
Z=W:50,!VISIBLE,SHOWDIM
R=W:50,!VISIBLE,SHOWDIM
T=W:50,!VISIBLE,SHOWDIM
U=W:50,VISIBLE,SHOWDIM
V=W:50,VISIBLE,SHOWDIM
W=W:50,!VISIBLE,SHOWDIM
Attribute=W:55,VISIBLE,DEFAULT:A,!SHOWDIM
Template=W:55,VISIBLE,DEFAULT:UV,!SHOWDIM
Comment=W:145,VISIBLE,!SHOWDIM
Options=W:165,VISIBLE,!SHOWDIM
Type=W:85,VISIBLE,!SHOWDIM
Size-U=W:55,!VISIBLE,DIM:um,SHOWDIM
Size-V=W:55,!VISIBLE,DIM:um,SHOWDIM
Points-U=W:55,!VISIBLE,DIM:px,SHOWDIM
Points-V=W:55,!VISIBLE,DIM:px,SHOWDIM
Dir=W:15,!VISIBLE,!SHOWDIM
Avg=W:25,!VISIBLE,!SHOWDIM
Pos1=W:85,VISIBLE,DIM:um,SHOWDIM
Pos2=W:85,VISIBLE,DIM:um,SHOWDIM
Pos3=W:85,VISIBLE,DIM:um,SHOWDIM
Link=W:25,VISIBLE,!SHOWDIM
File=W:482,VISIBLE,!SHOWDIM
Layer=W:80,VISIBLE,!SHOWDIM
Area=W:245,!VISIBLE,!SHOWDIM
DoseFactor=W:55,VISIBLE,!SHOWDIM
Dwelltime=W:55,!VISIBLE,DIM:ms,SHOWDIM
Stepsize=W:55,!VISIBLE,DIM:um,SHOWDIM
SplDwell=W:55,!VISIBLE,DIM:ms,SHOWDIM
SplStep=W:55,!VISIBLE,DIM:um,SHOWDIM
CurveStep=W:69,!VISIBLE,DIM:um,SHOWDIM
CurveDwell=W:55,!VISIBLE,DIM:ms,SHOWDIM
DotDwell=W:55,!VISIBLE,DIM:ms,SHOWDIM
FBMSArea=W:88,VISIBLE,DIM:mm/s,SHOWDIM
FBMSLines=W:81,VISIBLE,DIM:mm/s,SHOWDIM
SplDot=W:10,!VISIBLE,!SHOWDIM
Time=W:85,VISIBLE,!SHOWDIM
Timestamp=W:85,!VISIBLE,!SHOWDIM
Method=W:85,!VISIBLE,!SHOWDIM
Dot=W:20,!VISIBLE,!SHOWDIM

[DATA]
0,0.000000,0.000000,17.277540,0.000000,0.000000,0.000000,0.000000,7.722460,A,dUV,store currents,STAY,MACRO,,,,,,,,,,,C:\Quantum\User\Dewes\Scalable Architecture\Scripts\get currents.js,,,,,,,,,,,,,,,,,
0,0.000000,0.000000,17.277540,0.000000,0.000000,-3.620000,-0.720000,7.722460,A,UV,WA Qubit I,,MACRO,,,,,,,,,,,C:\Quantum\User\Dewes\Scalable Architecture\scripts\WAQubit1.js,,,,,,,,,,,,,,,,,
0,0.000000,0.000000,17.277540,0.000000,0.000000,0.000000,0.000000,7.722460,A,dUV,Qubit I,STAY,MACRO,,,,,,,,,,,C:\Quantum\User\Dewes\Scalable Architecture\scripts\expose_transmon.js,,,,,,,,,,,,,,,,,
0,0.000000,0.000000,17.277540,0.000000,0.000000,-3.950000,-0.450000,7.722460,A,UV,WA Qubit C I,,MACRO,,,,,,,,,,,C:\Quantum\User\Dewes\Scalable Architecture\scripts\WAQubitCapacitance1.js,,,,,,,,,,,,,,,,,
0,0.000000,0.000000,17.277540,0.000000,0.000000,0.000000,0.000000,7.722460,A,dUV,Qubit I Alignment Crosses,STAY,MACRO,,,,,,,,,,,C:\Quantum\User\Dewes\Scalable Architecture\scripts\expose_alignment_crosses.js,,,,,,,,,,,,,,,,,
0,0.000000,0.000000,17.277540,0.000000,0.000000,-3.950000,-0.450000,7.722460,A,UV,WA Qubit C I,,MACRO,,,,,,,,,,,C:\Quantum\User\Dewes\Scalable Architecture\scripts\WAQubitCapacitance1.js,,,,,,,,,,,,,,,,,
0,0.000000,0.000000,17.277540,0.000000,0.000000,0.000000,0.000000,7.722460,A,dUV,Qubit I C,STAY,MACRO,,,,,,,,,,,C:\Quantum\User\Dewes\Scalable Architecture\scripts\expose_transmon_capacitance.js,,,,,,,,,,,,,,,,,
0,0.000000,0.000000,17.277540,0.000000,0.000000,-1.820000,-0.700000,7.722460,A,UV,WA Qubit II,,MACRO,,,,,,,,,,,C:\Quantum\User\Dewes\Scalable Architecture\scripts\WAQubit2.js,,,,,,,,,,,,,,,,,
0,0.000000,0.000000,17.277540,0.000000,0.000000,0.000000,0.000000,7.722460,A,dUV,Qubit II,STAY,MACRO,,,,,,,,,,,C:\Quantum\User\Dewes\Scalable Architecture\scripts\expose_transmon.js,,,,,,,,,,,,,,,,,
0,0.000000,0.000000,17.277540,0.000000,0.000000,-2.150000,-0.450000,7.722460,A,UV,WA Qubit II C,,MACRO,,,,,,,,,,,C:\Quantum\User\Dewes\Scalable Architecture\scripts\WAQubitCapacitance2.js,,,,,,,,,,,,,,,,,
0,0.000000,0.000000,17.277540,0.000000,0.000000,0.000000,0.000000,7.722460,A,dUV,Qubit II C,STAY,MACRO,,,,,,,,,,,C:\Quantum\User\Dewes\Scalable Architecture\scripts\expose_transmon_capacitance.js,,,,,,,,,,,,,,,,,
0,0.000000,0.000000,17.277540,0.000000,0.000000,0.000000,0.000000,7.722460,A,dUV,Qubit II Alignment Crosses,STAY,MACRO,,,,,,,,,,,C:\Quantum\User\Dewes\Scalable Architecture\scripts\expose_alignment_crosses.js,,,,,,,,,,,,,,,,,
0,0.000000,0.000000,17.277540,0.000000,0.000000,1.820000,-0.700000,7.722460,A,UV,WA Qubit III,,MACRO,,,,,,,,,,,C:\Quantum\User\Dewes\Scalable Architecture\scripts\WAQubit3.js,,,,,,,,,,,,,,,,,
0,0.000000,0.000000,17.277540,0.000000,0.000000,0.000000,0.000000,7.722460,A,dUV,Qubit III,STAY,MACRO,,,,,,,,,,,C:\Quantum\User\Dewes\Scalable Architecture\scripts\expose_transmon.js,,,,,,,,,,,,,,,,,
0,0.000000,0.000000,17.277540,0.000000,0.000000,2.150000,-0.450000,7.722460,A,UV,WA Qubit III C,,MACRO,,,,,,,,,,,C:\Quantum\User\Dewes\Scalable Architecture\scripts\WAQubitCapacitance3.js,,,,,,,,,,,,,,,,,
0,0.000000,0.000000,17.277540,0.000000,0.000000,0.000000,0.000000,7.722460,A,dUV,Qubit III C,STAY,MACRO,,,,,,,,,,,C:\Quantum\User\Dewes\Scalable Architecture\scripts\expose_transmon_capacitance.js,,,,,,,,,,,,,,,,,
0,0.000000,0.000000,17.277540,0.000000,0.000000,0.000000,0.000000,7.722460,A,dUV,Qubit III Alignment Crosses,STAY,MACRO,,,,,,,,,,,C:\Quantum\User\Dewes\Scalable Architecture\scripts\expose_alignment_crosses.js,,,,,,,,,,,,,,,,,
0,0.000000,0.000000,17.277540,0.000000,0.000000,3.620000,-0.660000,7.722460,A,UV,WA Qubit IV,,MACRO,,,,,,,,,,,C:\Quantum\User\Dewes\Scalable Architecture\scripts\WAQubit4.js,,,,,,,,,,,,,,,,,
0,0.000000,0.000000,17.277540,0.000000,0.000000,0.000000,0.000000,7.722460,A,dUV,Qubit IV,STAY,MACRO,,,,,,,,,,,C:\Quantum\User\Dewes\Scalable Architecture\scripts\expose_transmon.js,,,,,,,,,,,,,,,,,
0,0.000000,0.000000,17.277540,0.000000,0.000000,3.950000,-0.450000,7.722460,A,UV,WA Qubit IV C,,MACRO,,,,,,,,,,,C:\Quantum\User\Dewes\Scalable Architecture\scripts\WAQubitCapacitance4.js,,,,,,,,,,,,,,,,,
0,0.000000,0.000000,17.277540,0.000000,0.000000,0.000000,0.000000,7.722460,A,dUV,Qubit IV C,STAY,MACRO,,,,,,,,,,,C:\Quantum\User\Dewes\Scalable Architecture\scripts\expose_transmon_capacitance.js,,,,,,,,,,,,,,,,,
0,0.000000,0.000000,17.277540,0.000000,0.000000,0.000000,0.000000,7.722460,A,dUV,Qubit IV Alignment Crosses,STAY,MACRO,,,,,,,,,,,C:\Quantum\User\Dewes\Scalable Architecture\scripts\expose_alignment_crosses.js,,,,,,,,,,,,,,,,,
0,0.000000,0.000000,17.277540,0.000000,0.000000,-4.200000,-0.387000,7.722460,A,UV,WA JBA I,,MACRO,,,,,,,,,,,C:\Quantum\User\Dewes\Scalable Architecture\scripts\WAJBAT.js,,,,,,,,,,,,,,,,,
0,0.000000,0.000000,17.277540,0.000000,0.000000,0.000000,0.000000,7.722460,A,dUV,JBA I,STAY,MACRO,,,,,,,,,,,C:\Quantum\User\Dewes\Scalable Architecture\scripts\expose_jba.js,,,,,,,,,,,,,,,,,
0,0.000000,0.000000,17.277540,0.000000,0.000000,-2.400000,-0.381000,7.722460,A,UV,WA JBA II,,MACRO,,,,,,,,,,,C:\Quantum\User\Dewes\Scalable Architecture\scripts\WAJBAT.js,,,,,,,,,,,,,,,,,
0,0.000000,0.000000,17.277540,0.000000,0.000000,0.000000,0.000000,7.722460,A,dUV,JBA II,STAY,MACRO,,,,,,,,,,,C:\Quantum\User\Dewes\Scalable Architecture\scripts\expose_jba.js,,,,,,,,,,,,,,,,,
0,0.000000,0.000000,17.277540,0.000000,0.000000,1.900000,-0.375000,7.722460,A,UV,WA JBA III,,MACRO,,,,,,,,,,,C:\Quantum\User\Dewes\Scalable Architecture\scripts\WAJBAT.js,,,,,,,,,,,,,,,,,
0,0.000000,0.000000,17.277540,0.000000,0.000000,0.000000,0.000000,7.722460,A,dUV,JBA III,STAY,MACRO,,,,,,,,,,,C:\Quantum\User\Dewes\Scalable Architecture\scripts\expose_jba.js,,,,,,,,,,,,,,,,,
0,0.000000,0.000000,17.277540,0.000000,0.000000,3.700000,-0.363000,7.722460,A,UV,WA JBA IV,,MACRO,,,,,,,,,,,C:\Quantum\User\Dewes\Scalable Architecture\scripts\WAJBAT.js,,,,,,,,,,,,,,,,,
0,0.000000,0.000000,17.277540,0.000000,0.000000,0.000000,0.000000,7.722460,A,dUV,JBA IV,STAY,MACRO,,,,,,,,,,,C:\Quantum\User\Dewes\Scalable Architecture\scripts\expose_jba.js,,,,,,,,,,,,,,,,,
0,0.000000,0.000000,17.277540,0.000000,0.000000,-4.000000,-1.300000,7.722460,A,UV,Twin JBA I,,MACRO,,,,,,,,,,,C:\Quantum\User\Dewes\Scalable Architecture\scripts\twin_jba.js,,,,,,,,,,,,,,,,,
0,0.000000,0.000000,17.277540,0.000000,0.000000,4.000000,-1.300000,7.722460,A,UV,Twin JBA II,,MACRO,,,,,,,,,,,C:\Quantum\User\Dewes\Scalable Architecture\scripts\twin_jba.js,,,,,,,,,,,,,,,,,
0,0.000000,0.000000,17.277540,0.000000,0.000000,-4.000000,1.300000,7.722460,A,UV,Twin JBA III,,MACRO,,,,,,,,,,,C:\Quantum\User\Dewes\Scalable Architecture\scripts\twin_jba.js,,,,,,,,,,,,,,,,,
0,0.000000,0.000000,17.277540,0.000000,0.000000,4.000000,1.300000,7.722460,A,UV,Twin JBA IV,,MACRO,,,,,,,,,,,C:\Quantum\User\Dewes\Scalable Architecture\scripts\twin_jba.js,,,,,,,,,,,,,,,,,
0,0.000000,0.000000,17.277540,0.000000,0.000000,-3.500000,-1.300000,7.722460,A,UV,Twin Qubit I,,MACRO,,,,,,,,,,,C:\Quantum\User\Dewes\Scalable Architecture\scripts\twin_qubit.js,,,,,,,,,,,,,,,,,
0,0.000000,0.000000,17.277540,0.000000,0.000000,-3.000000,-1.300000,7.722460,A,UV,Twin Qubit II,,MACRO,,,,,,,,,,,C:\Quantum\User\Dewes\Scalable Architecture\scripts\twin_qubit.js,,,,,,,,,,,,,,,,,
0,0.000000,0.000000,17.277540,0.000000,0.000000,3.000000,-1.300000,7.722460,A,UV,Twin Qubit III,,MACRO,,,,,,,,,,,C:\Quantum\User\Dewes\Scalable Architecture\scripts\twin_qubit.js,,,,,,,,,,,,,,,,,
0,0.000000,0.000000,17.277540,0.000000,0.000000,3.500000,-1.300000,7.722460,A,UV,Twin Qubit IV,,MACRO,,,,,,,,,,,C:\Quantum\User\Dewes\Scalable Architecture\scripts\twin_qubit.js,,,,,,,,,,,,,,,,,
0,0.000000,0.000000,17.277540,0.000000,0.000000,-3.500000,1.300000,7.722460,A,UV,Twin Qubit V,,MACRO,,,,,,,,,,,C:\Quantum\User\Dewes\Scalable Architecture\scripts\twin_qubit.js,,,,,,,,,,,,,,,,,
0,0.000000,0.000000,17.277540,0.000000,0.000000,-3.000000,1.300000,7.722460,A,UV,Twin Qubit VI,,MACRO,,,,,,,,,,,C:\Quantum\User\Dewes\Scalable Architecture\scripts\twin_qubit.js,,,,,,,,,,,,,,,,,
0,0.000000,0.000000,17.277540,0.000000,0.000000,3.000000,1.300000,7.722460,A,UV,Twin Qubit VII,,MACRO,,,,,,,,,,,C:\Quantum\User\Dewes\Scalable Architecture\scripts\twin_qubit.js,,,,,,,,,,,,,,,,,
0,0.000000,0.000000,17.277540,0.000000,0.000000,3.500000,1.300000,7.722460,A,UV,Twin Qubit VIII,,MACRO,,,,,,,,,,,C:\Quantum\User\Dewes\Scalable Architecture\scripts\twin_qubit.js,,,,,,,,,,,,,,,,,
