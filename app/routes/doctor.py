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
        if request.is_json == False:
            return jsonify({"message": "failed, please input in json format", "status": 0}), 400
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
            if req not in request.json:
                return jsonify({"message": f"failed, {req} is required"}), 400
        if Doctor.query.filter_by(username=request.json["username"]).first():
            return jsonify({"message": "username already existed"}), 400
        doctor = Doctor(
            name=request.json["name"],
            username=request.json["username"],
            password=request.json["password"],
            gender=request.json["gender"],
            birthdate=request.json["birthdate"],
            work_start_time=request.json["work_start_time"],
            work_end_time=request.json["work_end_time"],
        )
        try:
            db.session.add(doctor)
            db.session.commit()
            data = {
                "name": doctor.name,
                "username": doctor.username,
                "gender": doctor.gender.value,
                "birthdate": doctor.birthdate.strftime("%Y-%m-%d"),
                "work_start_time": doctor.work_start_time.strftime("%H:%M:%S"),
                "work_end_time": doctor.work_end_time.strftime("%H:%M:%S"),
            }
            return jsonify({"data": data, "message": "doctor created", "status": 1}), 201
        except:
            return jsonify({"message": "failed creating doctor"}), 500
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
def doctor_by_id(id):
    doctor = Doctor.query.filter_by(id=id).first()
    if doctor is None:
        return jsonify({"message": "doctor not found"}), 404
    if request.method == "PUT":
        if request.is_json == False:
            return jsonify({"message": "failed, please input in json format", "status": 0}), 400
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
            if req not in request.json:
                return jsonify({"message": f"failed, {req} is required"}), 400
        try:
            password = bcrypt.generate_password_hash(request.json["password"]).decode('utf-8')
            doctor.name = request.json["name"]
            doctor.username = request.json["username"]
            doctor.password = password
            doctor.gender = request.json["gender"]
            doctor.birthdate = request.json["birthdate"]
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
