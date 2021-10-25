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
    doc = Doctor.query.filter_by(id=request.form.get("doctor_id")).first()
    pat = Patient.query.filter_by(id=request.form.get("patient_id")).first()
    doc_start = datetime.strptime(str(doc.work_start_time), "%H:%M:%S")
    doc_end = datetime.strptime(str(doc.work_end_time), "%H:%M:%S")
    app_time = datetime.strptime(request.form.get("datetime").split(" ")[1], "%H:%M:%S")
    if app_time < doc_start or app_time > doc_end:
        return jsonify({"message": "failed, out of the doctor work time"})

    if request.method == "POST":
        required = [
            "patient_id",
            "doctor_id",
            "datetime",
            "status",
        ]
        for req in required:
            if req not in request.form:
                return jsonify({"message": f"failed, {req} is required"}), 400
        data = Appointment(
            patient_id=request.form.get("patient_id"),
            doctor_id=request.form.get("doctor_id"),
            datetime=request.form.get("datetime"),
            status=request.form.get("status"),
            diagnose="null" if request.form.get("diagnose") is None else request.form.get("diagnose"),
            notes="null" if request.form.get("notes") is None else request.form.get("notes"),
        )
        try:
            db.session.add(data)
            db.session.commit()
            return jsonify({"data": data.status.value, "message": "success", "status": 1}), 201
        except:
            return jsonify({"message": "failed"}), 500
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
def get_appointment_by_id(id):
    appointment = Appointment.query.filter_by(id=id).first()
    if appointment is None:
        return jsonify({"message": "appointment not found"}), 404
    if request.method == "PUT":
        required = [
            "patient_id",
            "doctor_id",
            "datetime",
            "status",
            "diagnose",
            "notes",
        ]
        for req in required:
            if req not in request.form:
                return jsonify({"message": f"failed, {req} is required"}), 400
        # try:
        appointment.patient_id =request.form.get("patient_id"),
        appointment.doctor_id =request.form.get("doctor_id"),
        appointment.datetime =request.form.get("datetime"),
        appointment.status =request.form.get("status"),
        appointment.diagnose =request.form.get("diagnose"),
        appointment.notes =request.form.get("notes"),
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
    return jsonify({"data": data, "message": "get employee", "status": 1}), 200
