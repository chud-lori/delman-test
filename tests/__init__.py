# """
# run from python using flask run
# """

# # from app import create_app

# # # create instance app
# # app = create_app()

# # if __name__ == '__main__':
# #     # run in debug mode
# #     app.run(debug=True)

# from app import db
# from app.models import Employee

# try:
#     db.drop_all()
#     db.create_all()
#     db.session.commit()
#     print("tables created")
# except:
#     print("Failed creating table")

# try:
#     db.session.add(Employee(name="admin", username="admin", password="admin11132", gender="female", birthdate="2021-01-01"))
#     db.session.commit()
#     print("data seeded")
# except:
#     print("seed failed")

