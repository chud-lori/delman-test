from flask import Blueprint, jsonify, request
import app.jwt as jwt
from app.models import Patient
from app import db

patient_bp = Blueprint("patient_bp", __name__)


@patient_bp.route("/patients", methods=["GET", "POST"])
@jwt.is_login
def patients():
    if request.method == "POST":
        required = [
            "name",
            "gender",
            "birthdate",
            "no_ktp",
            "address",
        ]
        for req in required:
            if req not in request.form:
                return jsonify({"message": f"failed, {req} is required"}), 400
        if Patient.query.filter_by(no_ktp=request.form.get("no_ktp")).first():
            return jsonify({"message": "no_ktp already existed"}), 400
        patient = Patient(
            name=request.form.get("name"),
            gender=request.form.get("gender"),
            birthdate=request.form.get("birthdate"),
            no_ktp=request.form.get("no_ktp"),
            address=request.form.get("address"),
            vaccine_type=request.form.get("vaccine_type"),
            vaccine_count=request.form.get("vaccine_count"),
        )
        try:
            db.session.add(patient)
            db.session.commit()
            data = {
                "name": patient.name,
                "gender": patient.gender.value,
                "birthdate": patient.birthdate.strftime("%Y-%m-%d"),
                "no_ktp": patient.no_ktp,
                "address": patient.address,
                "vaccine_type": patient.vaccine_type,
                "vaccine_count": patient.vaccine_count,
            }
            return jsonify({"data": data, "message": "patient created", "status": 1}), 201
        except:
            return jsonify({"message": "failed"}), 500
    pat_all = Patient.query.all()
    patients = [
        {
            "name": pat.name,
            "gender": pat.gender.value,
            "birthdate": pat.birthdate.strftime("%Y-%m-%d"),
            "no_ktp": pat.no_ktp,
            "address": pat.address,
            "vaccine_type": pat.vaccine_type,
            "vaccine_count": pat.vaccine_count,
        }
        for pat in pat_all
    ]
    return jsonify({"data": patients, "message": "success", "status": 1}), 200


@patient_bp.route("/patients/<id>", methods=["GET", "PUT", "DELETE"])
@jwt.is_login
def get_employee_by_id(id):
    patient = Patient.query.filter_by(id=id).first()
    if patient is None:
        return jsonify({"message": "patient not found"}), 404
    if request.method == "PUT":
        required = [
            "name",
            "gender",
            "birthdate",
            "no_ktp",
            "address",
            "vaccine_type",
            "vaccine_count",
        ]
        for req in required:
            if req not in request.form:
                return jsonify({"message": f"failed, {req} is required"}), 400
        try:
            patient.name = request.form.get("name")
            patient.gender = request.form.get("gender")
            patient.birthdate = request.form.get("birthdate")
            patient.no_ktp = request.form.get("no_ktp")
            patient.address = request.form.get("address")
            patient.vaccine_type = request.form.get("vaccine_type")
            patient.vaccine_count = request.form.get("vaccine_count")
            db.session.commit()
            patient = {
                "name": patient.name,
                "gender": patient.gender.value,
                "birthdate": patient.birthdate.strftime("%Y-%m-%d"),
                "no_ktp": patient.no_ktp,
                "address": patient.address,
                "vaccine_type": patient.vaccine_type,
                "vaccine_count": patient.vaccine_count,
            }
            return (
                jsonify({"data": patient, "message": "patient updated", "status": 1}),
                200,
            )
        except:
            return jsonify({"message": "update failed", "status": 0}), 500
    if request.method == "DELETE":
        try:
            Patient.query.filter_by(id=id).delete()
            db.session.commit()
            print("delete success")
            return jsonify({"message": "patient deleted", "status": 1}), 200
        except:
            return jsonify({"message": "delete failed", "status": 0}), 500
    data = {
        "name": patient.name,
        "gender": patient.gender.value,
        "birthdate": patient.birthdate.strftime("%Y-%m-%d"),
        "no_ktp": patient.no_ktp,
        "address": patient.address,
        "vaccine_type": patient.vaccine_type,
        "vaccine_count": patient.vaccine_count,
    }
    return jsonify({"data": data, "message": "get patient", "status": 1}), 200


@patient_bp.route("/schedule")
def schedule_vaccine():
    from app.scheduler import schedule_patient

    return schedule_patient()
