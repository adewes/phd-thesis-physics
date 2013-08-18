       //////////////////////////////////
      //       Vacuum Squeezing       //
     //                              //
    //       Transmon Capacitance   //
   //////////////////////////////////

var structure="C10";

// Coordinates for the writefield trG
var mag=100;
 

//Alignment and correction parameters
var resetCorrec=1;                       // wether to reset correction for magnification mag
var previousMag=0;                    	// previous magnification for reading corresponding corrections. None if 0
var systematicCorrec="";		  // systematic correction to add to the UV coordinates. None if ""
var ask=0;                               // ask confirmation during the process

//Column parameters
var voltage=25;
var spotSize1=1;                         // spotsize for squid
var spotSize2=2;
var spotSize3=3;
var spotSize4=4;                        // spotsize for capacitance and contact pads
var spotSize5=5;                        // spotsize for capacitance and contact pads

//Exposure parameters
var dwellTimeMin=0.001;                 // minimum dwelltime in ms (Elphy unit)

var expose1=1;           //wether to expose capa
var expose4=1;           //wether to expose capa undercut
var expose5=1;           //wether to expose capa undercut

listOfLayer1 = new Array(1,-1);      // Set of layers to be exposed for capacitance
listOfLayer4 = new Array(4,-1);      // Set of layers to be exposed for capa undercut
listOfLayer5 = new Array(5,-1);      // Set of layers to be exposed for capa undercut

var factor = 1.0;

var dose1=250*factor;                  // capa
var dose4=250*factor;                  // undercut capa
var dose5=250*factor;                  // undercut capa

var relDoseMin1=1;                      // minimum relative dose of elements in list of layer
var relDoseMin4=0.1;
var relDoseMin5=1;

var showCalculate=0;                    // wether to show dialog boxes for checking parameters
var showTime=0;                         // wether to calculate and show the exposure time

var reInit=0;                            // Re initialize the SEM if 1

//**********************************************************************
// MAIN CODE SECTION
//**********************************************************************
var error=0;

// Capa and mid pads exposure
App.Exec("CorrectWD()");

if (Quantro_SetColumnParam(voltage,spotSize5,mag,0)==0){error=1};  //spot 4
if (error==0){probeCurrent=Quantro_GetCurrent(2,0);if (probeCurrent==0){error=1}};
if ((error==0)&& expose1!=0){Quantro_Expose(structure,listOfLayer1,mag,dose1,relDoseMin1,dwellTimeMin,probeCurrent,showCalculate,showTime)};   //capa

App.Exec("CorrectWD()");
// Undercut exposure
if (Quantro_SetColumnParam(voltage,spotSize5,mag,0)==0){error=1};  //spot 4
if (error==0){probeCurrent=Quantro_GetCurrent(2,0);if (probeCurrent==0){error=1}};
if ((error==0)&& expose4!=0){Quantro_Expose(structure,listOfLayer4,mag,dose4,relDoseMin4,dwellTimeMin,probeCurrent,showCalculate,showTime)};   // capa undercut

App.Exec("CorrectWD()");
// Undercut exposure
if (Quantro_SetColumnParam(voltage,spotSize5,mag,0)==0){error=1};  //spot 4
if (error==0){probeCurrent=Quantro_GetCurrent(2,0);if (probeCurrent==0){error=1}};
if ((error==0)&& expose5!=0){Quantro_Expose(structure,listOfLayer5,mag,dose5,relDoseMin5,dwellTimeMin,probeCurrent,showCalculate,showTime)};   // capa undercut

Quantro_SetColumnParam(voltage,1,mag,1);

if ((error==0)&& reInit==1){Quantro_ReInitialize()};
