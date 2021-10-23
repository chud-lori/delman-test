from app import db
import enum

class Gender(enum.Enum):
    male = 'male'
    female = 'female'

class Employee(db.Model):
    """Model for datasets."""

    __tablename__ = 'employees'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    username = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    gender = db.Column(db.Enum(Gender), nullable=False)
    birthdate = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return '<Name {}>'.format(self.name)
        # return {'name': self.name, 'username': self.username, 'gender': self.gender.value, 'birthdate': birthdate}



# class Admin(db.Model):
#     """Model for admin"""

#     __tablename__ = 'admins'
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(20), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     password = db.Column(db.String(60), nullable=False)

#     def __repr__(self):
#         return '<Username {}>'.format(self.username)