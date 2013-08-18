var directory ="C:\\Quantum\\User\\Dewes\\Vacuum Squeezing\\gds";
var file= "2011_09_23_All Structures.csf";
var structure="A2";
var alignment = 0;
var ManualMarksLayer=63;                 // Layer of the structure that contains boxes for manual alignment
var AutoMarksLayer=61;                   // Layer of the structure that contains boxes for manual alignment

var centerU=-3840,centerV=0;        	   // center of the working area for left transmon in UV coordinates.
var mag=500;
var error=0;

var area1=Quantro_WorkingArea(mag,centerU,centerV);
Quantro_OpenAndShow(directory + file,structure,1,area1);

App.Exec("CorrectWD()");

if (alignment == 1)
{
  Quantro_DoAlignment(structure,mag,ManualMarksLayer,AutoMarksLayer,1);
}
