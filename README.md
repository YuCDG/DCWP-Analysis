# Department of Consumer & Worker Protection (DCWP) Data
The department of consumer and worker protection(DCWP) records several kinds violations and compliance needs charged against businesses and properties. This information is kept in order to help maintain compliance and benefit the public in terms of safety and fiduciary relations.<br>

My project's purpose is to transform and clean data from 2022 to 2024 for NY. The main usage of this data should be to allow auditors to visualize patterns in summary and over time. It should also facilitate categorizations by various nominal data types. Additionally, the data can be useable for location based analysis via zip codes combined with longitudes & latitudes.<br>

Ultimately, this can help determine where the DCWP should focus and what kinds of violations take the most precedent.

# APP_KEY Generation
URL: https://data.cityofnewyork.us/
<br> Above is the link to which you can create a free account. You must then navigate to your profile and to developer options. There you will be able to generate an APP key that you can paste into *APP_TOKEN* variable.
<br> <br>
Alternatively if you've been given the config.py file, which contains the APP_KEY, you can place that into a folder containing all project files (as made available in this repository) and run the import code under *Data Retrieval* section.

# Code Instruction
For starters create a folder to download the follow folder & file into:<br>
dfclasses<br>Main_Code<br>nyczones.shp<br>
![image](https://github.com/user-attachments/assets/924cd916-c12d-42fb-a594-1137970646cc)


Once you've created your APP key on NYCOpenData, you can copy and paste the string value into the **APP_TOKEN** variable within **Data Retrieval** section. The rest of the code should all be run from top to bottom, in that order.<br>
![image](https://github.com/user-attachments/assets/5648cffb-e3b6-4565-9cc8-495f6c0e89c0)

<br><br>

# Data Information
## Data Source
https://data.cityofnewyork.us/Business/Department-of-Consumer-and-Worker-Protection-DCWP-/5fn4-dr26/about_data
## Data Dictionary
https://data.cityofnewyork.us/api/views/5fn4-dr26/files/5eceefdb-8b07-4581-a3f8-4495e7072973?download=true&filename=DCA%20Charges%20Data%20Dictionary.pdf
## Data Structure
The working data has been queried to contain only information in NY state from 2022-2024. <br>
**rows**: 53679 <br>
**columns**: 23
## Data Dimensions
**Categorical**<br>
Record ID | Certificate Number | Business Name | Industry | Borough | City | State | Zip | 
Building Number | Unit Type | Unit | Street | Street 2 | Description | Charge | Outcome | <br>
**Numerical**<br>
Violation Date | Charge Count | Counts Settled | Counts Guilty | Counts Not Guilty | Longitude | Latitude



