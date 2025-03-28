# Department of Consumer & Worker Protection (DCWP) Data
The department of consumer and worker protection(DCWP) records several kinds violations and compliance needs charged against businesses and properties. This information is kept in order to help maintain compliance and benefit the public in terms of safety and fiduciary relations.<br>

My project's purpose is to transform and clean data from 2022 to 2024 for NY. The main usage of this data should be to allow auditors to visualize patterns in summary and over time. It should also facilitate categorizations by various nominal data types. Additionally, the data can be useable for location based analysis via zip codes combined with longitudes & latitudes.<br>

Ultimately, this can help determine where the DCWP should focus and what kinds of violations take the most precedent.

# Discovery & Suggestions
The most prominent businesses that stand up in terms of charges is the e-cig & tobacco retailers, alongside  Secondhand dealerships for cars. The tobacco and e-cig violation counts stood out in 2022 but, we reason that this might be due to the Clean Indoor Air Act(CIAA). During which there were stronger regulations against flavored tobacco products.
<br>
On the other hand, the Secondhand Dealerships had high legal charges in 2022 that were concentrated in Brooklyn and Queens. This saturation didn't carry over to 2023 but, it does mean that the DCWP may wish to keep that industry on a shorter leash moving forward.

# APP_KEY Generation
URL: https://data.cityofnewyork.us/
<br> Above is the link to which you can create a free account. You must then navigate to your profile and to developer options. There you will be able to generate an APP key that you can paste into *APP_TOKEN* variable.
<br> <br>
Alternatively if you've been given the config.py file, which contains the APP_KEY, you can place that into a folder containing all project files (as made available in this repository) and run the import code under *Data Retrieval* section.

# Code Instruction
For starters create a folder to download the follow folder & file into:<br>
dfclasses<br>Main_Code<br>nyczones.shp<br>

Once you've created your APP key on NYCOpenData, you can copy and paste the string value into the **APP_TOKEN** variable within **Data Retrieval** section. The rest of the code should all be run from top to bottom, in that order.<br>

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

# Graphs
## Second Hand Dealerships
![image](https://github.com/user-attachments/assets/7ed38e41-922e-4058-ba5c-99d9c9896f63) 
In this geograph, the violations for second hand auto dealerships are plotted. We see that despite the outstanding number of charges, the locations are more specific.
<br>
## Tobacco & E-Cig Retailers
![image](https://github.com/user-attachments/assets/17d4393c-1d0d-4142-bec2-aab9ec5f9046)
In this geograph, we see a very spread out plotting of enforcement violations for the tobacco/ e-cig retailer industry. This is more reasonable and lends credability to the theory that the spike in violation was due to the new 2022 enforcement for flavored tobacco.





