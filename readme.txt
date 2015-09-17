To configure SixSwiss.xlsm:

1. Open SixSwiss.xlsm and open the Developer tab on the ribbon. If it is not enabled, read this:

https://msdn.microsoft.com/en-us/library/bb608625.aspx

2. In the Developer tab, click the View Code button in the toolbar.

3. The top section of the "Sheet2 (Get SIX Swiss data)" code file contains the configuration for
   the script. Change the following settings:
   
   3.1 "localFileDir" specifies where the script stores temporary downloaded files. Change this to any local
	   directory.
	   
   3.2 "analysisFileDir" specifies the directory where the script will look for the analysis file.
   
To use SixSwiss.xlsm:

1. Copy today's analysis file to the directory specified by "analysisFileDir" in the script configuration.

2. Click the "Get SIX Swiss data" button in the Excel sheet. Running the script will probably take a while.
   The script is done when the mouse cursor turns back into an arrow and Excel becomes responsive again.
   
3. A list of ISIN IDs found in the SIX Swiss files but not in the analysis file are pasted into the G
   column.
   
