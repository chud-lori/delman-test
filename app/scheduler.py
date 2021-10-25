from flask import jsonify
from app import db
from app.models import Patient
from google.cloud import bigquery
from google.oauth2 import service_account

credentials = service_account.Credentials.from_service_account_file("credbig.json")
client = bigquery.Client(credentials=credentials)

QUERY = "select * from `interview_mock_data.vaccine_data`"


def vaccine_data():
    query_job = client.query(QUERY)
    rows = query_job.result()
    data = {}
    for row in rows:
        data[str(row.no_ktp)] = [str(row.vaccine_type), row.vaccine_count]
    return data


# d = vaccine_data()
# for i in d:
#     print(d.get(i)[0])


def schedule_patient():
    data = vaccine_data()
    try:    
        for vac in data:
            print(vac)
            patient = Patient.query.filter_by(no_ktp=vac).first()
            if patient is None:
                print("patient not found")
            patient.vaccine_type = data.get(vac)[0]
            patient.vaccine_count = data.get(vac)[1]
            db.session.commit()
            patient = {
                "name": patient.name,
                "gender": patient.gender.value,
                "birthdate": patient.birthdate,
                "no_ktp": patient.no_ktp,
                "address": patient.address,
                "vaccine_type": patient.vaccine_type,
                "vaccine_count": patient.vaccine_count,
            }
        print("vaccine data updated")
        return (
            jsonify({"data": patient, "message": "patient updated", "status": 1}),
            200,
        )
    except:
        return jsonify({"message": "update failed", "status": 0}), 500
