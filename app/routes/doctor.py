from flask import Blueprint, json, jsonify, redirect, request
from datetime import date, datetime
from sqlalchemy import text
from app import db, bcrypt
import app.jwt as jwt
import random, string
from app.models import Doctor

doctor_bp = Blueprint("doctor_bp", __name__)


@doctor_bp.route("/doctors", methods=["GET", "POST"])
@jwt.is_login
def doctors():
    if request.method == "POST":
        required = [
            "name",
            "username",
            "password",
            "gender",
            "birthdate",
            "work_start_time",
            "work_end_time",
        ]
        for req in required:
            if req not in request.form:
                return jsonify({"message": f"failed, {req} is required"}), 400
        if Doctor.query.filter_by(username=request.form.get("username")).first():
            return jsonify({"message": "username already existed"}), 400
        data = Doctor(
            name=request.form.get("name"),
            username=request.form.get("username"),
            password=request.form.get("password"),
            gender=request.form.get("gender"),
            birthdate=request.form.get("birthdate"),
            work_start_time=request.form.get("work_start_time"),
            work_end_time=request.form.get("work_end_time"),
        )
        # try:
        db.session.add(data)
        db.session.commit()
        return jsonify({"data": data.name, "message": "success", "status": 1}), 201
        # except:
        #     return jsonify({"message": "failed"}), 500
    doc_all = Doctor.query.all()
    doctors = [
        {
            "name": doct.name,
            "username": doct.username,
            "gender": doct.gender.value,
            "birthdate": doct.birthdate.strftime("%Y-%m-%d"),
            "work_start_time": doct.work_start_time.strftime("%H:%M:%S"),
            "work_end_time": doct.work_end_time.strftime("%H:%M:%S"),
        }
        for doct in doc_all
    ]
    return jsonify({"data": doctors, "message": "success", "status": 1}), 200


@doctor_bp.route("/doctors/<id>", methods=["GET", "PUT", "DELETE"])
@jwt.is_login
def get_employee_by_id(id):
    doctor = Doctor.query.filter_by(id=id).first()
    if doctor is None:
        return jsonify({"message": "doctor not found"}), 404
    if request.method == "PUT":
        required = [
            "name",
            "username",
            "password",
            "gender",
            "birthdate",
            "work_start_time",
            "work_end_time",
        ]
        for req in required:
            if req not in request.form:
                return jsonify({"message": f"failed, {req} is required"}), 400
        try:
            doctor.name = request.form.get("name")
            doctor.username = request.form.get("username")
            doctor.password = request.form.get("password")
            doctor.gender = request.form.get("gender")
            doctor.birthdate = request.form.get("birthdate")
            db.session.commit()
            doctor = {
                "name": doctor.name,
                "username": doctor.username,
                "gender": doctor.gender.value,
                "birthdate": doctor.birthdate.strftime("%Y-%m-%d"),
                "work_start_time": doctor.work_start_time.strftime("%H:%M:%S"),
                "work_end_time": doctor.work_end_time.strftime("%H:%M:%S"),
            }
            return (
                jsonify({"data": doctor, "message": "doctor updated", "status": 1}),
                200,
            )
        except:
            return jsonify({"message": "update failed", "status": 0}), 500
    if request.method == "DELETE":
        try:
            Doctor.query.filter_by(id=id).delete()
            db.session.commit()
            print("delete success")
            return jsonify({"message": "doctor deleted", "status": 1}), 200
        except:
            return jsonify({"message": "delete failed", "status": 0}), 500
    data = {
        "name": doctor.name,
        "username": doctor.username,
        "gender": doctor.gender.value,
        "birthdate": doctor.birthdate.strftime("%Y-%m-%d"),
        "work_start_time": doctor.work_start_time.strftime("%H:%M:%S"),
        "work_end_time": doctor.work_end_time.strftime("%H:%M:%S"),
    }
    print(data)
    return jsonify({"data": data, "message": "get doctor", "status": 1}), 200
