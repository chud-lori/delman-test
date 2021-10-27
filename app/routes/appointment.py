from datetime import date
from flask import Blueprint, jsonify, request
import app.jwt as jwt
from app.models import Appointment, Doctor, Patient
from app import db
from datetime import datetime, time

appointment_bp = Blueprint("appointment_bp", __name__)


@appointment_bp.route("/appointments", methods=["GET", "POST"])
@jwt.is_login
def appointments():
    doc = Doctor.query.filter_by(id=request.json["doctor_id"]).first()
    pat = Patient.query.filter_by(id=request.json["patient_id"]).first()
    if doc is None:
        return jsonify({"message": "doctor not exist", "status": 0}), 404
    if pat is None:
        return jsonify({"message": "patient not exist", "status": 0}), 404
    doc_start = datetime.strptime(str(doc.work_start_time), "%H:%M:%S")
    doc_end = datetime.strptime(str(doc.work_end_time), "%H:%M:%S")
    app_time = datetime.strptime(request.json["datetime"].split(" ")[1], "%H:%M:%S")
    if app_time < doc_start or app_time > doc_end:
        return jsonify({"message": "failed, out of the doctor work time", "status": 0}), 400

    if request.method == "POST":
        if request.is_json == False:
            return jsonify({"message": "failed, please input in json format", "status": 0}), 400
        required = [
            "patient_id",
            "doctor_id",
            "datetime",
            "status",
        ]
        for req in required:
            if req not in request.json:
                return jsonify({"message": f"failed, {req} is required"}), 400
        appointment = Appointment(
            patient_id=request.json["patient_id"],
            doctor_id=request.json["doctor_id"],
            datetime=request.json["datetime"],
            status=request.json["status"],
            diagnose="null" if "diagnose" not in request.json else request.json["diagnose"],
            notes="null" if "notes" not in request.json else request.json["notes"],
        )
        try:
            db.session.add(appointment)
            db.session.commit()
            data = {
                "patient_id": appointment.patient_id,
                "doctor_id": appointment.doctor_id,
                "datetime": appointment.datetime.strftime("%Y-%m-%d %H:%M:%S"),
                "status": appointment.status.value,
                "diagnose": appointment.diagnose,
                "notes": appointment.notes,
            }
            return jsonify({"data": data, "message": "appoinment created", "status": 1}), 201
        except:
            return jsonify({"message": "failed creating appointment"}), 500
    appo_all = Appointment.query.all()
    appointment = [
        {
            "patient_id": appo.patient_id,
            "doctor_id": appo.doctor_id,
            "datetime": appo.datetime.strftime("%Y-%m-%d %H:%M:%S"),
            "status": appo.status.value,
            "diagnose": appo.diagnose,
            "notes": appo.notes,
        }
        for appo in appo_all
    ]
    return jsonify({"data": appointment, "message": "success", "status": 1}), 200


@appointment_bp.route("/appointments/<id>", methods=["GET", "PUT", "DELETE"])
@jwt.is_login
def appointment_by_id(id):
    appointment = Appointment.query.filter_by(id=id).first()
    if appointment is None:
        return jsonify({"message": "appointment not found"}), 404
    if request.method == "PUT":
        if request.is_json == False:
            return jsonify({"message": "failed, please input in json format", "status": 0}), 400
        required = [
            "patient_id",
            "doctor_id",
            "datetime",
            "status",
            "diagnose",
            "notes",
        ]
        for req in required:
            if req not in request.json:
                return jsonify({"message": f"failed, {req} is required"}), 400
        # try:
        print(request.json['status'])
        print(appointment.status)
        appointment.patient_id =request.json["patient_id"],
        appointment.doctor_id =request.json["doctor_id"],
        appointment.datetime =request.json["datetime"],
        appointment.status = "DONE",
        appointment.diagnose =request.json["diagnose"],
        appointment.notes =request.json["notes"],
        db.session.commit()
        appointment = {
            "patient_id": appointment.patient_id,
            "doctor_id": appointment.doctor_id,
            "datetime": appointment.datetime.strftime("%Y-%m-%d %H:%M:%S"),
            "status": appointment.status.value,
            "diagnose": appointment.diagnose,
            "notes": appointment.notes,
        }
        return (
            jsonify(
                {"data": appointment, "message": "appointment updated", "status": 1}
            ),
            200,
            )
        # except:
        #     return jsonify({"message": "update failed", "status": 0}), 500
    if request.method == "DELETE":
        try:
            Appointment.query.filter_by(id=id).delete()
            db.session.commit()
            print("delete success")
            return jsonify({"message": "appointment deleted", "status": 1}), 200
        except:
            return jsonify({"message": "delete failed", "status": 0}), 500
    data = {
        "patient_id": appointment.patient_id,
        "doctor_id": appointment.doctor_id,
        "datetime": appointment.datetime.strftime("%Y-%m-%d %H:%M:%S"),
        "status": appointment.status.value,
        "diagnose": appointment.diagnose,
        "notes": appointment.notes,
    }
    return jsonify({"data": data, "message": "get appointment", "status": 1}), 200
