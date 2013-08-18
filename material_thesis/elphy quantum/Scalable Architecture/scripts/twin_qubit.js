var directory ="C:\\Quantum\\User\\Dewes\\Scalable Architecture\\gds";
var file= "all structures.csf";
var structure="C10";
var ManualMarksLayer=63;                 // Layer of the structure that contains boxes for manual alignment
var AutoMarksLayer=61;                   // Layer of the structure that contains boxes for manual alignment

var centerU=-3620.000,centerV=-720.000;        	   // center of the working area for left transmon in UV coordinates.
var mag=1000;
var error=0;
var area1=Quantro_WorkingArea(mag,centerU,centerV);
Quantro_OpenAndShow(directory + file,structure,1,area1);

//Make the transmon...


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

//Exposure parameters
var dwellTimeMin=0.0007;                 // minimum dwelltime in ms (Elphy unit)

var expose7=1;           //wether to expose squids
var expose15=1;          //wether to expose squid undercut

listOfLayer7 = new Array(7,-1);      // Set of layers to be exposed for squid
listOfLayer15 = new Array(15,-1);    // Set of layers to be exposed for squid undercut

var factor = 1.0;

var dose7=250*factor;                  //squid
var dose15=250*factor;                 // undercut squid

var relDoseMin7=1;                       // minimum relative dose of elements in list of layer
var relDoseMin15=0.15;

var showCalculate=0;                    // wether to show dialog boxes for checking parameters
var showTime=0;                         // wether to calculate and show the exposure time

var reInit=0;                            // Re initialize the SEM if 1

//**********************************************************************
// MAIN CODE SECTION
//**********************************************************************
App.Exec("CorrectWD()");

// Transmon's squid exposure
if (Quantro_SetColumnParam(voltage,spotSize1,mag,0)==0){error=1}; //spot 1
if (error==0){probeCurrent=Quantro_GetCurrent(2,0);if (probeCurrent==0){error=1}};
if ((error==0)&& expose7!=0){Quantro_Expose(structure,listOfLayer7,mag,dose7,relDoseMin7,dwellTimeMin,probeCurrent,showCalculate,showTime)};      //squid
if ((error==0)&& expose15!=0){Quantro_Expose(structure,listOfLayer15,mag,dose15,relDoseMin15,dwellTimeMin,probeCurrent,showCalculate,showTime)}; //squid undercut

Quantro_SetColumnParam(voltage,1,mag,1);

if ((error==0)&& reInit==1){Quantro_ReInitialize()};

//Make the contact pad...
var spotSize6=6;			 // spotsize for pads
var spotSize7=7;			 // spotsize for pads
var mag=200;
var moveTo=1;
var verbose = 1;

//Exposure parameters
var dwellTimeMin=0.0008;                 // minimum dwelltime in ms (Elphy unit)

tune1=1;              //whether to tune current at that point

area=Quantro_WorkingArea(mag,-3500,1300,0);
Quantro_OpenAndShow(directory + file,structure,1,area);

listOfLayer8 = new Array(8,-1);		    // Set of layers to be exposed at large spot

var dose=250;                      	// µC/cm2

var relDoseMin=1;                       // minimum relative dose of elements in list of layer

var showCalculate=0;                    // wether to show dialog boxes for checking parameters
var showTime=0;                  // wether to calculate and show the exposure time

var reInit=0;                            // Re initialize the SEM if 1

//**********************************************************************
// MAIN CODE SECTION
//**********************************************************************

var probeCurrent,error=0,area1,area2;

if (Quantro_SetColumnParam(voltage,spotSize6,mag,0,1)==0){error=1};
if (error==0){probeCurrent=Quantro_GetCurrent(2,0);if (probeCurrent==0){error=1}};
//if (tune1!=0){Quantro_TuneCurrent()};

App.Exec("CorrectWD()");        
Quantro_Expose(structure,listOfLayer8,mag,dose,relDoseMin,dwellTimeMin,probeCurrent,showCalculate,showTime)

Quantro_SetColumnParam(voltage,spotSize1,mag,0,1);
if ((error==0)&& reInit==1){Quantro_ReInitialize()};

