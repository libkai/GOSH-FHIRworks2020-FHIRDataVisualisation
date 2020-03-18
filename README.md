# GOSH-FHIRworks2020-FHIRDataVisualisation
# Follow to steps below to setup web app

1. If you do not already have virtualenv on your local machine, do "pip install virtualenv"
2. Then do "virtualenv env", at this point an "env" folder should be created
3. If you're on windows, type ".\env\Scripts\activate.ps1" into your terminal
4. On the left of your terminal, you should see an "(env)", if you do, download the packages required by typing "pip install FHIR-Parser" and "pip install flask"
5. Type "$env:FLASK_APP = "app.py"
6. For development mode, type "$env:FLASK_ENV = "development"
7. Before you start the flask app, you should do "dotnet run" to make sure you have a connection to the FHIR Database
8. To run the web app, type "flask run --port=2000", then go to your browser and enter "localhost:2000" into the url


# How to use the web app

1. You can search for a patient by their name or ID
2. If you have found your patient, click the row in the table
3. You will be redirected to a page with 4 graphs, showing Blood Pressure, BMI and Body Measurements, Pain Severity Scores, and Mean Concentration
4. To go back to your list of patients, simply click on "FHIR Data Visualisation" on the top left corner of the web page
