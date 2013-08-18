       //////////////////////////////////
      //       Vacuum Squeezing       //
     //                              //
    //   Coupling Capacitance       //
   //////////////////////////////////

var structure = "A2";
//Alignment and correction parameters
var resetCorrec=0;                       // wether to reset correction for magnification mag
var previousMag=0;                    	// previous magnification for reading corresponding corrections. None if 0
var systematicCorrec="";		  // systematic correction to add to the UV coordinates. None if ""
var ask=1;                               // ask confirmation during the process

//Column parameters
var voltage=25;
var spotSize1=1;                         // spotsize for junction
var spotSize2=2;
var spotSize3=3;

var mag=500;
var moveTo=0;

//Exposure parameters
var dwellTimeMin=0.0007;                 // minimum dwelltime in ms (Elphy unit)

var expose5=1;           //wether to expose JBA junction
var expose9=1;           //wether to expose JBA junction undercut
var expose11=1;           //wether to expose JBA junction undercut

listOfLayer5 = new Array(5,-1);      // Set of layers to be exposed for JBA junction
listOfLayer9 = new Array(9,-1);      // Set of layers to be exposed for JBA junction undercut
listOfLayer11 = new Array(11,-1);      // Set of layers to be exposed for JBA junction undercut

var dose5=250;                  //JBA junction
var dose9=250;                  //JBA junction undercut
var dose11=250;                  //JBA junction undercut

var relDoseMin5=1;                       // minimum relative dose of elements in list of layer
var relDoseMin9=1;                       // minimum relative dose of elements in list of layer
var relDoseMin11=0.1;                      // minimum relative dose of elements in list of layer

var showCalculate=0;                    // wether to show dialog boxes for checking parameters
var showTime=0;                         // wether to calculate and show the exposure time

var reInit=0;                            // Re initialize the SEM if 1

//**********************************************************************
// MAIN CODE SECTION
//**********************************************************************

var probeCurrent,error=0,area1;
// Coupling Capacitance exposure


//The dose at which we want to start...
var currentDose = 0.5;

var currentU = -3.500;
var currentV = 0;

if (Quantro_SetColumnParam(voltage,spotSize1,mag,0)==0){error=1};   //Spot 1
if (error==0){probeCurrent=Quantro_GetCurrent(2,0);if (probeCurrent==0){error=1}};

while(currentDose<1.0)
{
   Quantro_MoveToUV(currentU,currentV,1,0);
   App.Exec("CorrectWD()");
   if ((error==0)&& expose5!=0){Quantro_Expose(structure,listOfLayer5,mag,dose5*currentDose,relDoseMin5,dwellTimeMin,probeCurrent,showCalculate,showTime)};
   if ((error==0)&& expose11!=0){Quantro_Expose(structure,listOfLayer11,mag,dose11*currentDose,relDoseMin11,dwellTimeMin,probeCurrent,showCalculate,showTime)};
   if ((error==0)&& expose9!=0){Quantro_Expose(structure,listOfLayer9,mag,dose9*currentDose,relDoseMin9,dwellTimeMin,probeCurrent,showCalculate,showTime)};
   currentU+=0.250;
   currentDose+=0.1;
}


Quantro_SetColumnParam(voltage,1,mag,0);

if ((error==0)&& reInit==1){Quantro_ReInitialize()};      
