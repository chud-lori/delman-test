from flask import (Blueprint, jsonify, redirect, request)
from flask.templating import render_template
from datetime import date, datetime

main_bp = Blueprint('main_bp', __name__)

@main_bp.errorhandler(404)
def page_not_found(e) -> tuple:
    """
        it will render if user got invalid route
    """
    return jsonify({'message': 'not found'}), 404