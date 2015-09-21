1. Both scripts require the Developer tab in Excel to be enabled on the ribbon. If it isn't already, follow this document:

	https://msdn.microsoft.com/en-us/library/bb608625.aspx

2. To configure SixSwiss.xlsm:

	2.1. In the Developer tab, click the View Code button in the toolbar.

	2.2. The top section of the "Sheet2 (Get SIX Swiss data)" code file contains the configuration forthe script. Change the following settings:
	   
	   2.2.1 "localFileDir" specifies where the script stores temporary downloaded files. Change this to any local directory.
		   
	   2.2.2 "analysisFileDir" specifies the directory where the script will look for the analysis file.
	   
3. To use SixSwiss.xlsm:

	3.1. Ensure today's analysis file is in the directory specified by "analysisFileDir" in the script configuration.

	3.2. Click the "Get SIX Swiss data" button in the Excel sheet. Running the script will probably take a while. The script is done when the mouse cursor turns back into an arrow and Excel becomes responsive again.
	   
	3.3. A list of ISIN IDs found in the SIX Swiss files but not in the analysis file are pasted into the G column.
   
4. To configure JiraFilters.xlsm:

	4.1 Install Python v3.4.3 or higher, the latest version can be downloaded at:

		https://www.python.org/downloads/

	4.2 Ensure that the Python install directory is in the PATH (or Path) environment variable. This guide describes how to set an environment variable: 

		http://www.microsoft.com/resources/documentation/windows/xp/all/proddocs/en-us/sysdm_advancd_environmnt_addchange_variable.mspx?mfr=true

		Note!: The PATH (or Path) variable probably already contains something. You should append the path to the end of the existing value, separating it with a semicolon (;). So, if the PATH variable already contains "C:\Windows\System32;C:\temp" and you want to add "C:\Python34" to it, the value should be "C:\Windows\System32;C:\temp;C:\Python34".

	4.3 Open the JiraFilters.xlsm file in Excel.

	4.4 In the Developer tab, click View code

	4.5 The top section of the "Sheet1 (Get Jira filters)" code file contains the configuration for the script. Change the following settings:

		* TEMPDIR - This should contain the full path to a local directory where the script can store temporary files. It should be empty except for files created by this script.

		* TARGETFILE - This should contain the full path to the workbook where the Jira data will be written.

		* REGULARDATA_SHEET - This should contain the name of the worksheet where the regulardata filter data will be written.

		* PLUGINDATA_SHEET - This should contain the name of the worksheet where the plugindata filter data will be written.

		* REGULARDATA_RANGE - This should contain the upper left cell where the regulardata filter data will be written. The data is four columns wide with an arbitrary number of rows.

		* PLUGINDATA_RANGE - This should contain the upper left cell where the plugindata filter data will be written. The data is four columns wide with an arbitrary number of rows.

		* REGULARDATA_FILTERID - This should contain the Jira ID of the regulardata filter.

		* PLUGINDATA_FILTERID - This should contain the Jira ID of the plugindata filter.

		* JIRA_USERNAME - This should contain the username used to retrieve the Jira data.

		* JIRA_URL - This should contain the url to the Jira site.

5. To run JiraFilters.xlsm: Run the script by clicking the button labeled "Get jira filters" in the single sheet. A popup dialogue will ask you for your Jira password.
