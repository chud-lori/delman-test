from app import db, bcrypt
import enum

class Gender(enum.Enum):
    male = 'male'
    female = 'female'

class Status(enum.Enum):
    IN_QUEUE = 'IN_QUEUE'
    DONE = 'DONE'
    CANCELLED = 'CANCELLED'

class Employee(db.Model):
    """Model for datasets."""

    __tablename__ = 'employees'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    username = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    gender = db.Column(db.Enum(Gender), nullable=False)
    birthdate = db.Column(db.Date, nullable=False)

    def __init__(self, name, username, password, gender, birthdate):
        password = bcrypt.generate_password_hash(password).decode('utf-8')
        self.password = password
        self.name = name
        self.username = username
        self.gender = gender
        self.birthdate = birthdate

    def __repr__(self):
        return '<Name {}>'.format(self.name)
        # return {'name': self.name, 'username': self.username, 'gender': self.gender.value, 'birthdate': birthdate}


class Doctor(db.Model):
    """Model for datasets."""

    __tablename__ = 'doctors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    username = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    gender = db.Column(db.Enum(Gender), nullable=False)
    birthdate = db.Column(db.Date, nullable=False)
    work_start_time = db.Column(db.Time, nullable=False)
    work_end_time = db.Column(db.Time, nullable=False)

    def __repr__(self):
        return '<Name {}>'.format(self.name)

class Patient(db.Model):
    """Model for datasets."""

    __tablename__ = 'patients'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    gender = db.Column(db.Enum(Gender), nullable=False)
    birthdate = db.Column(db.Date, nullable=False)
    no_ktp = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    vaccine_type = db.Column(db.String(255), nullable=True)
    vaccine_count = db.Column(db.Integer, nullable=True, default=0)

    def __repr__(self):
        return '<Name {}>'.format(self.name)

class Appointment(db.Model):
    """Model for datasets."""

    __tablename__ = 'appointments'
    id = db.Column(db.Integer, primary_key=True)
    doctor_id = db.Column(db.Integer, nullable=False)
    patient_id = db.Column(db.Integer, nullable=False)
    datetime = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.Enum(Status), nullable=False)
    diagnose = db.Column(db.Text, nullable=True)
    notes = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return '<Datetime {}>'.format(self.datetime)
