# USI Project

## About Data:
Due to the limitation of file size of GitHub, the 311 reports and DOHMH restaurant inspection data were not uploaded to the project repository. Although they are accessible on the NYC OpenData website, the data on that would be different from the one used in this project since they are real-time. To retrieve the same dataset as we used, filter both datasets by created date or inspection date to be from July 2010 to December 2015.    

VenueList.csv: a table which has information with regard to the geocoded restaurant locations in the DOHMH restaurant inspection record data. 

## Scripts:
SIP.ipynb: include all geocoding and data treatment process  
ARL.py: use this for Assocition Rule Learning  

## Reproducibility
Changing parameters in geocoding algorithm we used might affect the performance of cross-referencing process, which would also lead to a change in the result. A different geocoding method such as using GeoClient API by DoITT could also lead to a different result.  

We used pymining library for conducting ARL. Using a newer edition of the library or using other libraries could affect the result of ARL. Nonetheless, this should only result in minor differences as it comes to the final result.  