//Quantro_MeasureShift(hv1,spot1,mag1,hv2,spot2,mag2,scanName1,scanName2,referenceName,show)
//reset corrections at  x100 and x2000 to nominalzoom
Quantro_ResetCorrec(2000,true);Quantro_ResetCorrec(100,true);
//mesure the shift when switching from magnification 250 to 2000 spot 1
Quantro_MeasureShift(25,5,100,25,1,2000,"image 20mu","image 20mu and compare with Reference","reference 20mu.ssc",true);

//To read back the corrections 
//var shiftsMag100To2000="1,1,"+App.GetVariable("systematicCorrections.Shifts_V25S4M100_To_V25S1M2000")+",0,0"
//var correcMag2000From100=Quantro_ReverseCorrecString(shiftsMag100To2000);		               
//To set the corrections
//if (previousMag){Quantro_TransferCorrec(previousMag,magSquid,ask)}; 
//Quantro_AddCorrec(magSquid,correcMag2000From100,ask)