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
    """
    The main function to handle base route (/)
    It has validation and return proper data with proper information in json format
    """
    user = Employee.query.filter_by(username=request.form.get("username")).first()
    # if user is None:
    #     user = Doctor.query.filter_by(username=request.form.get('username')).first()
    if user is None:
        return jsonify({"message": "username not found"}), 404

    if bcrypt.check_password_hash(user.password, request.form.get("password")) == False:
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
        required = ["name", "username", "password", "gender", "birthdate"]
        for req in required:
            if req not in request.form:
                return jsonify({"message": f"failed, {req} is required"}), 400
        if Employee.query.filter_by(username=request.form.get("username")).first():
            return jsonify({"message": "username already existed"}), 400
        employee = Employee(
            name=request.form.get("name"),
            username=request.form.get("username"),
            password=request.form.get("password"),
            gender=request.form.get("gender"),
            birthdate=request.form.get("birthdate"),
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
            return jsonify({"message": "failed"}), 500
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
def get_employee_by_id(id):
    employee = Employee.query.filter_by(id=id).first()
    if employee is None:
        return jsonify({"message": "employee not found"}), 404
    if request.method == "PUT":
        required = ["name", "username", "password", "gender", "birthdate"]
        for req in required:
            if req not in request.form:
                return jsonify({"message": f"failed, {req} is required"}), 400
        try:
            password = request.form.get("password")
            employee.name = request.form.get("name")
            employee.username = request.form.get("username")
            employee.password = password
            employee.gender = request.form.get("gender")
            employee.birthdate = request.form.get("birthdate")
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
