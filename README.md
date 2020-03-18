# GOSH-FHIRworks2020-FHIRDataVisualisation
## Prerequisites
The following guide assumes you already have Python and pip installed on your local machine. If you do not have Python or pip, please install them.
For Windows, I will be using Windows PowerShell.

## Follow to steps below to setup web app

1. If you do not already have virtualenv on your local machine, do ```pip install virtualenv```
2. Then do ```virtualenv env```, at this point an "env" folder should be created
3. If you're on Windows, type ```.\env\Scripts\activate.ps1``` into your terminal
3. If you're on Mac/Linux, type ```source env/bin/activate``` into your terminal
4. On the left of your terminal, you should see an ```(env)```, if you do, that means you're in your virtual environment. Continue by  downloading the packages required
```bash
pip install FHIR-Parser 
pip install flask
```
5. Type ```$env:FLASK_APP = "app.py"```
6. For development mode, type ```$env:FLASK_ENV = "development"```
7. Before you start the flask app, you should make sure you have the [GOSH-FHIRworks2020 API](https://github.com/greenfrogs/FHIRworks_2020) on your local machine with the appsettings.json updated. Also make sure you have the [.NET Core 2.1 SDK 2.1.803](https://dotnet.microsoft.com/download/dotnet-core/2.1) installed. To check simply type ```dotnet``` 
8. If the requirements in step 7 are satisfied, simply type ```dotnet run``` to connect to the FHIR Database
9. To run the web app, type ```flask run --port=2000```, then go to your browser and enter **localhost:2000** into the url


## How to use the web app
1. You can search for a patient by their name or ID
2. If you have found your patient, click the row in the table
3. You will be redirected to a page with 4 graphs, showing Blood Pressure, BMI and Body Measurements, Pain Severity Scores, and Mean Concentration
4. To go back to your list of patients, simply click on "FHIR Data Visualisation" on the top left corner of the web page

## Web app Endpoints
``` bash
localhost:2000/
```
1. This will return a list of patients. You can search through the table and also decide how many entries you would like per page
``` bash
localhost:2000/observation/<patient.uuid>
```
2. This will return you the observations of the specified patient. 4 graphs will be displayed on the page along with their personal details
