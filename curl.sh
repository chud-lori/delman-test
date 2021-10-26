# Auth
curl -X POST --data 'username=admin&password=admin11132' http://localhost:5000/login

# Employee
# POST
curl -X POST -H "Authorization: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2Mzc3NzA2OTgsImlhdCI6MTYzNTE3ODY5OCwic3ViIjoxfQ.mm3CRPk2YlvakBo9BiZzJzF0znbaclK7Pj7Cofe55k4" --data 'name=employee one&username=employee1&gender=female&password=employee1234&birthdate=1994-07-13' http://localhost:5000/employees
# GET
curl -X GET -H "Authorization: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2Mzc3NzA2OTgsImlhdCI6MTYzNTE3ODY5OCwic3ViIjoxfQ.mm3CRPk2YlvakBo9BiZzJzF0znbaclK7Pj7Cofe55k4" http://localhost:5000/employees/1
# PUT
curl -X PUT -H "Authorization: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2Mzc3NzA2OTgsImlhdCI6MTYzNTE3ODY5OCwic3ViIjoxfQ.mm3CRPk2YlvakBo9BiZzJzF0znbaclK7Pj7Cofe55k4" --data 'name=employee one edited&username=employee1&gender=female&password=user1234&birthdate=1994-07-13' http://localhost:5000/employees/1
# DELETE
curl -X DELETE -H "Authorization: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2Mzc3NzA2OTgsImlhdCI6MTYzNTE3ODY5OCwic3ViIjoxfQ.mm3CRPk2YlvakBo9BiZzJzF0znbaclK7Pj7Cofe55k4" http://localhost:5000/employees/2


# Doctor
# POST
curl -X POST -H "Authorization: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2Mzc3NzA2OTgsImlhdCI6MTYzNTE3ODY5OCwic3ViIjoxfQ.mm3CRPk2YlvakBo9BiZzJzF0znbaclK7Pj7Cofe55k4" --data 'name=doctor one&username=doctor1&gender=female&password=doctor1234&birthdate=1980-02-22&work_start_time=07:00:00&work_end_time=19:00:00' http://localhost:5000/doctors
# GET
curl -X GET -H "Authorization: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2Mzc3NzA2OTgsImlhdCI6MTYzNTE3ODY5OCwic3ViIjoxfQ.mm3CRPk2YlvakBo9BiZzJzF0znbaclK7Pj7Cofe55k4" http://localhost:5000/doctors/1
# PUT
curl -X PUT -H "Authorization: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2Mzc3NzA2OTgsImlhdCI6MTYzNTE3ODY5OCwic3ViIjoxfQ.mm3CRPk2YlvakBo9BiZzJzF0znbaclK7Pj7Cofe55k4" --data 'name=doctor one edited&username=doctor1&gender=female&password=user1234&birthdate=1981-01-07&work_start_time=08:00:00&work_end_time=16:00:00' http://localhost:5000/doctors/1
# DELETE
curl -X DELETE -H "Authorization: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2Mzc3NzA2OTgsImlhdCI6MTYzNTE3ODY5OCwic3ViIjoxfQ.mm3CRPk2YlvakBo9BiZzJzF0znbaclK7Pj7Cofe55k4" http://localhost:5000/doctors/1


# Patient
# POST
curl -X POST -H "Authorization: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2Mzc3NzA2OTgsImlhdCI6MTYzNTE3ODY5OCwic3ViIjoxfQ.mm3CRPk2YlvakBo9BiZzJzF0znbaclK7Pj7Cofe55k4" --data 'name=patient one&gender=female&birthdate=1980-02-22&no_ktp=51710321121200017&address=Jakarta' http://localhost:5000/patients
# GET
curl -X GET -H "Authorization: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2Mzc3NzA2OTgsImlhdCI6MTYzNTE3ODY5OCwic3ViIjoxfQ.mm3CRPk2YlvakBo9BiZzJzF0znbaclK7Pj7Cofe55k4" http://localhost:5000/patients/1
# PUT
curl -X PUT -H "Authorization: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2Mzc3NzA2OTgsImlhdCI6MTYzNTE3ODY5OCwic3ViIjoxfQ.mm3CRPk2YlvakBo9BiZzJzF0znbaclK7Pj7Cofe55k4" --data 'name=patient one edited&gender=female&birthdate=1981-01-07&no_ktp=51710321121200017&address=Jakarta&vaccine_type=sinovac&vaccine_count=1' http://localhost:5000/patients/1
# DELETE
curl -X DELETE -H "Authorization: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2Mzc3NzA2OTgsImlhdCI6MTYzNTE3ODY5OCwic3ViIjoxfQ.mm3CRPk2YlvakBo9BiZzJzF0znbaclK7Pj7Cofe55k4" http://localhost:5000/patients/1


# Appointment
# POST
curl -X POST -H "Authorization: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2Mzc3NzA2OTgsImlhdCI6MTYzNTE3ODY5OCwic3ViIjoxfQ.mm3CRPk2YlvakBo9BiZzJzF0znbaclK7Pj7Cofe55k4" --data "doctor_id=1&patient_id=1&datetime=2021-03-12 13:00:00&status=IN_QUEUE" http://localhost:5000/appointments
# GET
curl -X GET -H "Authorization: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2Mzc3NzA2OTgsImlhdCI6MTYzNTE3ODY5OCwic3ViIjoxfQ.mm3CRPk2YlvakBo9BiZzJzF0znbaclK7Pj7Cofe55k4" http://localhost:5000/appointments/1
# PUT
curl -X PUT -H "Authorization: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2Mzc3NzA2OTgsImlhdCI6MTYzNTE3ODY5OCwic3ViIjoxfQ.mm3CRPk2YlvakBo9BiZzJzF0znbaclK7Pj7Cofe55k4" --data 'doctor_id=1&patient_id=1&datetime=2021-03-12 13:00:00&status=DONE&diagnose=goodaja&notes=eatfruit' http://localhost:5000/appointments/1
# DELETE
curl -X DELETE -H "Authorization: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2Mzc3NzA2OTgsImlhdCI6MTYzNTE3ODY5OCwic3ViIjoxfQ.mm3CRPk2YlvakBo9BiZzJzF0znbaclK7Pj7Cofe55k4" http://localhost:5000/appointments/1

# scheduler
curl http://localhost:5000/schedule