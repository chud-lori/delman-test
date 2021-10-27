from flask import Blueprint, json, jsonify, redirect, request
from datetime import date, datetime
from sqlalchemy import text
from app import db, bcrypt
import app.jwt as jwt
import random, string
from app.models import Employee, Doctor

employee_bp = Blueprint("employee_bp", __name__)


@employee_bp.route("/login", methods=["POST"])
def index() -> dict:
    if request.is_json == False:
        return jsonify({"message": "failed, please input in json format", "status": 0}), 400
    user = Employee.query.filter_by(username=request.json["username"]).first()
    if user is None:
        return jsonify({"message": "username not found"}), 404

    if bcrypt.check_password_hash(user.password, request.json["password"]) == False:
        return jsonify({"message": "wrong password"}), 403

    auth_token = jwt.encode_auth_token(user.id)

    response = {
        "data": {"name": user.name, "auth_token": auth_token.decode()},
        "message": "login success",
        "status": 1,
    }

    return jsonify(response), 200


@employee_bp.route("/employees", methods=["GET", "POST"])
@jwt.is_login
def employees():
    if request.method == "POST":
        if request.is_json == False:
            return jsonify({"message": "failed, please input in json format", "status": 0}), 400
        required = ["name", "username", "password", "gender", "birthdate"]
        for req in required:
            if req not in request.json:
                return jsonify({"message": f"failed, {req} is required"}), 400
        if Employee.query.filter_by(username=request.json["username"]).first():
            return jsonify({"message": "username already existed"}), 400
        employee = Employee(
            name=request.json["name"],
            username=request.json["username"],
            password=request.json["password"],
            gender=request.json["gender"],
            birthdate=request.json["birthdate"],
        )
        try:
            db.session.add(employee)
            db.session.commit()
            data = {
                "name": employee.name,
                "username": employee.username,
                "gender": employee.gender.value,
                "birthdate": employee.birthdate.strftime("%Y-%m-%d"),
            }
            return jsonify({"data": data, "message": "employee created", "status": 1}), 201
        except:
            return jsonify({"message": "failed creating employee"}), 500
    emp_all = Employee.query.all()
    employees = [
        {
            "name": emp.name,
            "username": emp.username,
            "gender": emp.gender.value,
            "birthdate": emp.birthdate.strftime("%Y-%m-%d"),
        }
        for emp in emp_all
    ]
    return jsonify({"data": employees, "message": "success", "status": 1}), 200


@employee_bp.route("/employees/<id>", methods=["GET", "PUT", "DELETE"])
@jwt.is_login
def employee_by_id(id):
    employee = Employee.query.filter_by(id=id).first()
    if employee is None:
        return jsonify({"message": "employee not found"}), 404
    if request.method == "PUT":
        if request.is_json == False:
            return jsonify({"message": "failed, please input in json format", "status": 0}), 400
        required = ["name", "username", "password", "gender", "birthdate"]
        for req in required:
            if req not in request.json:
                return jsonify({"message": f"failed, {req} is required"}), 400
        try:
            password = bcrypt.generate_password_hash(request.json["password"]).decode('utf-8')
            employee.name = request.json["name"]
            employee.username = request.json["username"]
            employee.password = password
            employee.gender = request.json["gender"]
            employee.birthdate = request.json["birthdate"]
            db.session.commit()
            employee = {
                "name": employee.name,
                "username": employee.username,
                "gender": employee.gender.value,
                "birthdate": employee.birthdate.strftime("%Y-%m-%d"),
            }
            return (
                jsonify({"data": employee, "message": "employee updated", "status": 1}),
                200,
            )
        except:
            return jsonify({"message": "update failed", "status": 0}), 500
    if request.method == "DELETE":
        try:
            Employee.query.filter_by(id=id).delete()
            db.session.commit()
            print("delete success")
            return jsonify({"message": "employee deleted", "status": 1}), 200
        except:
            return jsonify({"message": "delete failed", "status": 0}), 500
    data = {
        "name": employee.name,
        "username": employee.username,
        "gender": employee.gender.value,
        "birthdate": employee.birthdate.strftime("%Y-%m-%d"),
    }
    return jsonify({"data": data, "message": "get employee", "status": 1}), 200
