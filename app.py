from flask import Flask, render_template, url_for
from fhir_parser import FHIR
from datetime import datetime
import time

app = Flask(__name__)

fhir = FHIR()

@app.route('/')
def index():
    allPatients = fhir.get_all_patients()
    return render_template('index.html', allPatients = allPatients)

@app.route('/observation/<string:id>')
def observation(id):
    patient = fhir.get_patient(id)
    observations = fhir.get_patient_observations(id)
    bodyDict = {
        "date": [],
        "height": [],
        "weight": [],
        "bmi": []
    }
    bloodPressureDict = {
        "date" : [],
        "bloodPressure": [],
        "diastolicBloodPressure": [],
        "systolicBloodPressure": []
    }
    painSeverityDict = {
        "date": [],
        "score": []
    }
    meanConcentrationDict = {
        "date": [],
        "mcv": [],
        "mch": [],
        "mchc": []
    }

    tempDateList = []
    observationList = []

    for observation in observations:
        if observation.components[0].display == "Blood Pressure":
            formattedDate = time.mktime(observation.effective_datetime.timetuple()) * 1000
            tempDateList.append(formattedDate)
            observationList.append(observation)
    
    tempDateList.sort()

    for i in range(len(tempDateList)):
        for j in range(len(observationList)):
            if tempDateList[i] == time.mktime(observationList[j].effective_datetime.timetuple()) * 1000:
                bloodPressureDict["date"].append(tempDateList[i])
                bloodPressureDict["bloodPressure"].append(observationList[j].components[0].value)
                bloodPressureDict["diastolicBloodPressure"].append(observationList[j].components[1].value)
                bloodPressureDict["systolicBloodPressure"].append(observationList[j].components[2].value)

    bodyDateList = []
    bodyObservationList = []

    for observation in observations:
        if observation.components[0].display == "Body Height" or observation.components[0].display == "Body Weight" or observation.components[0].display == "Body Mass Index":
            formattedDate = (time.mktime(observation.effective_datetime.timetuple()) * 1000)
            if formattedDate not in bodyDateList:
                bodyDateList.append(formattedDate)
            bodyObservationList.append(observation)

    bodyDateList.sort()

    for i in range(len(bodyDateList)):
        for j in range(0, len(bodyObservationList)):
            if bodyDateList[i] == time.mktime(bodyObservationList[j].effective_datetime.timetuple()) * 1000:
                if bodyDateList[i] not in bodyDict["date"]:
                    bodyDict["date"].append(bodyDateList[i])
                if bodyObservationList[j].components[0].display == "Body Height":
                    bodyDict["height"].append(bodyObservationList[j].components[0].value)
                elif bodyObservationList[j].components[0].display == "Body Weight":
                    bodyDict["weight"].append(bodyObservationList[j].components[0].value)
                elif bodyObservationList[j].components[0].display == "Body Mass Index":
                    bodyDict["bmi"].append(bodyObservationList[j].components[0].value)

    painDateList = []
    painObservationList = []

    for observation in observations:
        if observation.components[0].display == "Pain severity - 0-10 verbal numeric rating [Score] - Reported":
            formattedDate = (time.mktime(observation.effective_datetime.timetuple()) * 1000)
            if formattedDate not in painDateList:
                painDateList.append(formattedDate)
            painObservationList.append(observation)

    painDateList.sort()

    for i in range(len(painDateList)):
        for j in range(0, len(painObservationList)):
            if painDateList[i] == time.mktime(painObservationList[j].effective_datetime.timetuple()) * 1000:
                if painDateList[i] not in painSeverityDict["date"]:
                    painSeverityDict["date"].append(painDateList[i])
                if painObservationList[j].components[0].display == "Pain severity - 0-10 verbal numeric rating [Score] - Reported":
                    painSeverityDict["score"].append(painObservationList[j].components[0].value)

    meanConcDateList = []
    meanConcObservationList = []

    for observation in observations:
        if observation.components[0].display == "MCV [Entitic volume] by Automated count" or observation.components[0].display == "MCHC [Mass/volume] by Automated count" or observation.components[0].display == "MCH [Entitic mass] by Automated count":
            formattedDate = (time.mktime(observation.effective_datetime.timetuple()) * 1000)
            if formattedDate not in meanConcDateList:
                meanConcDateList.append(formattedDate)
            meanConcObservationList.append(observation)

    meanConcDateList.sort()

    for i in range(len(meanConcDateList)):
        for j in range(0, len(meanConcObservationList)):
            if meanConcDateList[i] == time.mktime(meanConcObservationList[j].effective_datetime.timetuple()) * 1000:
                if meanConcDateList[i] not in meanConcentrationDict["date"]:
                    meanConcentrationDict["date"].append(meanConcDateList[i])
                if meanConcObservationList[j].components[0].display == "MCV [Entitic volume] by Automated count":
                    meanConcentrationDict["mcv"].append(meanConcObservationList[j].components[0].value)
                elif meanConcObservationList[j].components[0].display == "MCHC [Mass/volume] by Automated count":
                    meanConcentrationDict["mchc"].append(meanConcObservationList[j].components[0].value)
                elif meanConcObservationList[j].components[0].display == "MCH [Entitic mass] by Automated count":
                    meanConcentrationDict["mch"].append(meanConcObservationList[j].components[0].value)

    return render_template('observation.html', observations = observations, patient = patient, bloodPressureDict = bloodPressureDict, bodyDict = bodyDict, painSeverityDict = painSeverityDict, meanConcentrationDict = meanConcentrationDict)

if __name__ == "__main__":
    app.run(debug=True)