"""
initiation file for the app
this file invoked from setup.py outstide
this represent the corpe/ directory
"""

from flask import Flask
from app.config import Config
from app.db import connect_db
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

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
        app.register_blueprint(employee_bp)
        
        return app
