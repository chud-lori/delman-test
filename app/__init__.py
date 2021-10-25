"""
initiation file for the app
this file invoked from setup.py outstide
this represent the corpe/ directory
"""

from flask import Flask
from app.config import Config
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
# from apscheduler.schedulers.background import BackgroundScheduler

# def sensor():
#     """ Function for test purposes. """
#     print("Scheduler is alive!")

# sched = BackgroundScheduler(daemon=True)
# sched.add_job(sensor,'interval',seconds=6)
# sched.start()

# db = connect_db()
db = SQLAlchemy()
bcrypt = Bcrypt()

def create_app(config=Config):
    """
    end point of the app
    """
    # Initiate flask object and its config
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config)
    bcrypt.init_app(app)
    db.init_app(app)
    from app.route import page_not_found
    app.register_error_handler(404, page_not_found)

    # run route from the app context
    with app.app_context():
        # Import routes
        from app.routes.employee import employee_bp
        from app.routes.doctor import doctor_bp
        from app.routes.patient import patient_bp
        from app.routes.appointment import appointment_bp
        app.register_blueprint(employee_bp)
        app.register_blueprint(doctor_bp)
        app.register_blueprint(patient_bp)
        app.register_blueprint(appointment_bp)
        
        return app
