      //////////////////////////////////
     //        Vacuum Squeezing      //
    //          Test pads           //
   //////////////////////////////////


//Column parameters
var voltage=25;
var spotSize1=1;
var spotSize6=6;			 // spotsize for pads
var spotSize7=7;			 // spotsize for pads
var mag=200;
var moveTo=1;
var verbose = 1;

var directory ="C:\\Quantum\\User\\Dewes\\Scalable Architecture\\gds";
var file= "all structures.csf";
var structure="C10";

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
