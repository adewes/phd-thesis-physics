
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
0,0.000000,0.000000,17.277540,0.000000,0.000000,-3.680000,-0.680000,7.722460,A,UV,WA Qubit 1,,MACRO,,,,,,,,,,,C:\Quantum\User\Dewes\Scalable Architecture\scripts\b8\wa_qubit_1.js,,,,,,,,,,,,,,,,,
0,0.000000,0.000000,17.277540,0.000000,0.000000,0.000000,0.000000,7.722460,A,dUV,Qubit 1,STAY,MACRO,,,,,,,,,,,C:\Quantum\User\Dewes\Scalable Architecture\scripts\b8\expose_transmon.js,,,,,,,,,,,,,,,,,
0,0.000000,0.000000,17.277540,0.000000,0.000000,-3.950000,-0.460000,7.722460,A,UV,WA Resonator 1,,MACRO,,,,,,,,,,,C:\Quantum\User\Dewes\Scalable Architecture\scripts\b8\wa_resonator_1.js,,,,,,,,,,,,,,,,,
0,0.000000,0.000000,17.277540,0.000000,0.000000,0.000000,0.000000,7.722460,A,dUV,Resonator 1,STAY,MACRO,,,,,,,,,,,C:\Quantum\User\Dewes\Scalable Architecture\scripts\b8\expose_resonator.js,,,,,,,,,,,,,,,,,
0,0.000000,0.000000,17.277540,0.000000,0.000000,-4.200000,-0.390000,7.722460,A,UV,WA JBA 1,,MACRO,,,,,,,,,,,C:\Quantum\User\Dewes\Scalable Architecture\scripts\b8\wa_jba_1.js,,,,,,,,,,,,,,,,,
0,0.000000,0.000000,17.277540,0.000000,0.000000,0.000000,0.000000,7.722460,A,dUV,JBA 1,STAY,MACRO,,,,,,,,,,,C:\Quantum\User\Dewes\Scalable Architecture\scripts\b8\expose_jba.js,,,,,,,,,,,,,,,,,
0,0.000000,0.000000,17.277540,0.000000,0.000000,-1.880000,-0.680000,7.722460,A,UV,WA Qubit 2,,MACRO,,,,,,,,,,,C:\Quantum\User\Dewes\Scalable Architecture\scripts\b8\wa_qubit_2.js,,,,,,,,,,,,,,,,,
0,0.000000,0.000000,17.277540,0.000000,0.000000,0.000000,0.000000,7.722460,A,dUV,Qubit 2,STAY,MACRO,,,,,,,,,,,C:\Quantum\User\Dewes\Scalable Architecture\scripts\b8\expose_transmon.js,,,,,,,,,,,,,,,,,
0,0.000000,0.000000,17.277540,0.000000,0.000000,-2.150000,-0.460000,7.722460,A,UV,WA Resonator 2,,MACRO,,,,,,,,,,,C:\Quantum\User\Dewes\Scalable Architecture\scripts\b8\wa_resonator_2.js,,,,,,,,,,,,,,,,,
0,0.000000,0.000000,17.277540,0.000000,0.000000,0.000000,0.000000,7.722460,A,dUV,Resonator 2,STAY,MACRO,,,,,,,,,,,C:\Quantum\User\Dewes\Scalable Architecture\scripts\b8\expose_resonator.js,,,,,,,,,,,,,,,,,
0,0.000000,0.000000,17.277540,0.000000,0.000000,-2.400000,-0.390000,7.722460,A,UV,WA JBA 2,,MACRO,,,,,,,,,,,C:\Quantum\User\Dewes\Scalable Architecture\scripts\b8\wa_jba_2.js,,,,,,,,,,,,,,,,,
0,0.000000,0.000000,17.277540,0.000000,0.000000,0.000000,0.000000,7.722460,A,dUV,JBA 2,STAY,MACRO,,,,,,,,,,,C:\Quantum\User\Dewes\Scalable Architecture\scripts\b8\expose_jba.js,,,,,,,,,,,,,,,,,
0,0.000000,0.000000,17.277540,0.000000,0.000000,1.880000,-0.680000,7.722460,A,UV,WA Qubit 3,,MACRO,,,,,,,,,,,C:\Quantum\User\Dewes\Scalable Architecture\scripts\b8\wa_qubit_3.js,,,,,,,,,,,,,,,,,
0,0.000000,0.000000,17.277540,0.000000,0.000000,0.000000,0.000000,7.722460,A,dUV,Qubit 3,STAY,MACRO,,,,,,,,,,,C:\Quantum\User\Dewes\Scalable Architecture\scripts\b8\expose_transmon.js,,,,,,,,,,,,,,,,,
0,0.000000,0.000000,17.277540,0.000000,0.000000,2.150000,-0.460000,7.722460,A,UV,WA Resonator 3,,MACRO,,,,,,,,,,,C:\Quantum\User\Dewes\Scalable Architecture\scripts\b8\wa_resonator_3.js,,,,,,,,,,,,,,,,,
0,0.000000,0.000000,17.277540,0.000000,0.000000,0.000000,0.000000,7.722460,A,dUV,Resonator 3,STAY,MACRO,,,,,,,,,,,C:\Quantum\User\Dewes\Scalable Architecture\scripts\b8\expose_resonator.js,,,,,,,,,,,,,,,,,
0,0.000000,0.000000,17.277540,0.000000,0.000000,2.400000,-0.390000,7.722460,A,UV,WA JBA 3,,MACRO,,,,,,,,,,,C:\Quantum\User\Dewes\Scalable Architecture\scripts\b8\wa_jba_3.js,,,,,,,,,,,,,,,,,
0,0.000000,0.000000,17.277540,0.000000,0.000000,0.000000,0.000000,7.722460,A,dUV,JBA 3,STAY,MACRO,,,,,,,,,,,C:\Quantum\User\Dewes\Scalable Architecture\scripts\b8\expose_jba.js,,,,,,,,,,,,,,,,,
0,0.000000,0.000000,17.277540,0.000000,0.000000,3.680000,-0.680000,7.722460,A,UV,WA Qubit 4,,MACRO,,,,,,,,,,,C:\Quantum\User\Dewes\Scalable Architecture\scripts\b8\wa_qubit_4.js,,,,,,,,,,,,,,,,,
0,0.000000,0.000000,17.277540,0.000000,0.000000,0.000000,0.000000,7.722460,A,dUV,Qubit 4,STAY,MACRO,,,,,,,,,,,C:\Quantum\User\Dewes\Scalable Architecture\scripts\b8\expose_transmon.js,,,,,,,,,,,,,,,,,
0,0.000000,0.000000,17.277540,0.000000,0.000000,3.950000,-0.460000,7.722460,A,UV,WA Resonator 4,,MACRO,,,,,,,,,,,C:\Quantum\User\Dewes\Scalable Architecture\scripts\b8\wa_resonator_4.js,,,,,,,,,,,,,,,,,
0,0.000000,0.000000,17.277540,0.000000,0.000000,0.000000,0.000000,7.722460,A,dUV,Resonator 4,STAY,MACRO,,,,,,,,,,,C:\Quantum\User\Dewes\Scalable Architecture\scripts\b8\expose_resonator.js,,,,,,,,,,,,,,,,,
0,0.000000,0.000000,17.277540,0.000000,0.000000,4.200000,-0.390000,7.722460,A,UV,WA JBA 4,,MACRO,,,,,,,,,,,C:\Quantum\User\Dewes\Scalable Architecture\scripts\b8\wa_jba_4.js,,,,,,,,,,,,,,,,,
0,0.000000,0.000000,17.277540,0.000000,0.000000,0.000000,0.000000,7.722460,A,dUV,JBA 4,STAY,MACRO,,,,,,,,,,,C:\Quantum\User\Dewes\Scalable Architecture\scripts\b8\expose_jba.js,,,,,,,,,,,,,,,,,
0,0.000000,0.000000,17.277540,0.000000,0.000000,-3.000000,-1.300000,7.722460,A,UV,Twin JBA 1,,MACRO,,,,,,,,,,,C:\Quantum\User\Dewes\Scalable Architecture\scripts\b8\twin_jba.js,,,,,,,,,,,,,,,,,
0,0.000000,0.000000,17.277540,0.000000,0.000000,-2.500000,-1.300000,7.722460,A,UV,Twin JBA 2,,MACRO,,,,,,,,,,,C:\Quantum\User\Dewes\Scalable Architecture\scripts\b8\twin_jba.js,,,,,,,,,,,,,,,,,
0,0.000000,0.000000,17.277540,0.000000,0.000000,2.500000,-1.300000,7.722460,A,UV,Twin JBA 3,,MACRO,,,,,,,,,,,C:\Quantum\User\Dewes\Scalable Architecture\scripts\b8\twin_jba.js,,,,,,,,,,,,,,,,,
0,0.000000,0.000000,17.277540,0.000000,0.000000,3.000000,-1.300000,7.722460,A,UV,Twin JBA 4,,MACRO,,,,,,,,,,,C:\Quantum\User\Dewes\Scalable Architecture\scripts\b8\twin_jba.js,,,,,,,,,,,,,,,,,
0,0.000000,0.000000,17.277540,0.000000,0.000000,-3.000000,1.300000,7.722460,A,UV,Twin JBA 5,,MACRO,,,,,,,,,,,C:\Quantum\User\Dewes\Scalable Architecture\scripts\b8\twin_jba.js,,,,,,,,,,,,,,,,,
0,0.000000,0.000000,17.277540,0.000000,0.000000,-2.500000,1.300000,7.722460,A,UV,Twin JBA 6,,MACRO,,,,,,,,,,,C:\Quantum\User\Dewes\Scalable Architecture\scripts\b8\twin_jba.js,,,,,,,,,,,,,,,,,
0,0.000000,0.000000,17.277540,0.000000,0.000000,2.500000,1.300000,7.722460,A,UV,Twin JBA 7,,MACRO,,,,,,,,,,,C:\Quantum\User\Dewes\Scalable Architecture\scripts\b8\twin_jba.js,,,,,,,,,,,,,,,,,
0,0.000000,0.000000,17.277540,0.000000,0.000000,3.000000,1.300000,7.722460,A,UV,Twin JBA 8,,MACRO,,,,,,,,,,,C:\Quantum\User\Dewes\Scalable Architecture\scripts\b8\twin_jba.js,,,,,,,,,,,,,,,,,
0,0.000000,0.000000,17.277540,0.000000,0.000000,-4.000000,-1.300000,7.722460,A,UV,Twin Qubit 1,,MACRO,,,,,,,,,,,C:\Quantum\User\Dewes\Scalable Architecture\scripts\b8\twin_qubit.js,,,,,,,,,,,,,,,,,
0,0.000000,0.000000,17.277540,0.000000,0.000000,-3.500000,-1.300000,7.722460,A,UV,Twin Qubit 2,,MACRO,,,,,,,,,,,C:\Quantum\User\Dewes\Scalable Architecture\scripts\b8\twin_qubit.js,,,,,,,,,,,,,,,,,
0,0.000000,0.000000,17.277540,0.000000,0.000000,3.500000,-1.300000,7.722460,A,UV,Twin Qubit 3,,MACRO,,,,,,,,,,,C:\Quantum\User\Dewes\Scalable Architecture\scripts\b8\twin_qubit.js,,,,,,,,,,,,,,,,,
0,0.000000,0.000000,17.277540,0.000000,0.000000,4.500000,-1.300000,7.722460,A,UV,Twin Qubit 4,,MACRO,,,,,,,,,,,C:\Quantum\User\Dewes\Scalable Architecture\scripts\b8\twin_qubit.js,,,,,,,,,,,,,,,,,
0,0.000000,0.000000,17.277540,0.000000,0.000000,-4.000000,1.300000,7.722460,A,UV,Twin Qubit 5,,MACRO,,,,,,,,,,,C:\Quantum\User\Dewes\Scalable Architecture\scripts\b8\twin_qubit.js,,,,,,,,,,,,,,,,,
0,0.000000,0.000000,17.277540,0.000000,0.000000,-3.500000,1.300000,7.722460,A,UV,Twin Qubit 6,,MACRO,,,,,,,,,,,C:\Quantum\User\Dewes\Scalable Architecture\scripts\b8\twin_qubit.js,,,,,,,,,,,,,,,,,
0,0.000000,0.000000,17.277540,0.000000,0.000000,3.500000,1.300000,7.722460,A,UV,Twin Qubit 7,,MACRO,,,,,,,,,,,C:\Quantum\User\Dewes\Scalable Architecture\scripts\b8\twin_qubit.js,,,,,,,,,,,,,,,,,
0,0.000000,0.000000,17.277540,0.000000,0.000000,4.500000,1.300000,7.722460,A,UV,Twin Qubit 8,,MACRO,,,,,,,,,,,C:\Quantum\User\Dewes\Scalable Architecture\scripts\b8\twin_qubit.js,,,,,,,,,,,,,,,,,
