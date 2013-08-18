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

var expose1=1;           //wether to expose capa
var expose4=1;           //wether to expose capa undercut

listOfLayer1 = new Array(1,-1);      // Set of layers to be exposed for capacitance
listOfLayer4 = new Array(4,-1);      // Set of layers to be exposed for capa undercut

var factor = 1.0;

var dose1=250*factor;                  // capa
var dose4=250*factor;                  // undercut capa

var relDoseMin1=1;                      // minimum relative dose of elements in list of layer
var relDoseMin4=0.1;

var showCalculate=0;                    // wether to show dialog boxes for checking parameters
var showTime=0;                         // wether to calculate and show the exposure time

var reInit=0;       

//**********************************************************************
// MAIN CODE SECTION
//**********************************************************************

var probeCurrent,error=0,area1;
// Coupling Capacitance exposure


//The dose at which we want to start...
var currentDose = 0.5;

var currentU = -3.500;
var currentV = 0.500;

while(currentDose<1.2)
{
   Quantro_MoveToUV(currentU,currentV,1,0);
   App.Exec("CorrectWD()");

   if (Quantro_SetColumnParam(voltage,spotSize3,mag,0)==0){error=1};  //spot 3
   if (error==0){probeCurrent=Quantro_GetCurrent(2,0);if (probeCurrent==0){error=1}};
   if ((error==0)&& expose1!=0){Quantro_Expose(structure,listOfLayer1,mag,dose1*currentDose,relDoseMin1,dwellTimeMin,probeCurrent,showCalculate,showTime)};   //capa

   App.Exec("CorrectWD()");

   if (Quantro_SetColumnParam(voltage,spotSize1,mag,0)==0){error=1};  //spot 1
   if (error==0){probeCurrent=Quantro_GetCurrent(2,0);if (probeCurrent==0){error=1}};
   if ((error==0)&& expose4!=0){Quantro_Expose(structure,listOfLayer4,mag,dose4*currentDose,relDoseMin4,dwellTimeMin,probeCurrent,showCalculate,showTime)};   // capa undercut

   currentU+=0.250;
   currentDose+=0.1;
}

Quantro_SetColumnParam(voltage,1,mag,0);

if ((error==0)&& reInit==1){Quantro_ReInitialize()};



