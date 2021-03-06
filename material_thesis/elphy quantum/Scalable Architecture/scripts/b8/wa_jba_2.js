var directory ="C:\\Quantum\\User\\Dewes\\Scalable Architecture\\gds";
var file= "all structures.csf";
var structure="B8";

var alignment = 1;
var ManualMarksLayer=63;                 // Layer of the structure that contains boxes for manual alignment
var AutoMarksLayer=61;                   // Layer of the structure that contains boxes for manual alignment

var centerU=-2400,centerV=-390;        	   // center of the working area for left transmon in UV coordinates.
var mag=500;
var error=0;

var area1=Quantro_WorkingArea(mag,centerU,centerV);
Quantro_OpenAndShow(directory + file,structure,1,area1);

App.Exec("CorrectWD()");

if (alignment == 1)
{
  Quantro_DoAlignment(structure,mag,ManualMarksLayer,AutoMarksLayer,1);
}
