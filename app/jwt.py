import datetime
import functools
from flask.json import jsonify
import jwt
from app.config import Config
from flask import request

def encode_auth_token(user_id):
    """
    Generates the Auth Token
    :return: string
    """
    try:
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=30),
            'iat': datetime.datetime.utcnow(),
            'sub': user_id
        }
        return jwt.encode(
            payload,
            '\r\x9d\xc4\x99\xcai\xb0OMy\x99y[C\xff\xa93\x98\x83\x04D\xe7\xc6\xa6',
            algorithm='HS256'
        )
    except Exception as e:
        return e


def decode_auth_token(auth_token):
    """
    Decodes the auth token
    :param auth_token:
    :return: integer|string
    """
    try:
        payload = jwt.decode(auth_token, '\r\x9d\xc4\x99\xcai\xb0OMy\x99y[C\xff\xa93\x98\x83\x04D\xe7\xc6\xa6')
        return payload['sub']
    except jwt.ExpiredSignatureError:
        # return 'Signature expired. Please log in again.'
        return False
    except jwt.InvalidTokenError:
        # return 'Invalid token. Please log in again.'
        return False

# def is_slogin(func):
#     def inner():
#         token = request.headers.get('Authorization')
#         if token is None or decode_auth_token(token) == False:
#             print("Invalid")
#             return jsonify({'message': 'invalid or not found token'}), 403
#         return func()

#         # return func(a, b)
#     return inner

def is_login(func):
    """
    This decorator only runs the function passed if the user's access_level is admin.
    """
    @functools.wraps(func)
    def secure_func(*args, **kwargs):
        token = request.headers.get('Authorization')
        if token is None or decode_auth_token(token) == False:
            print("Invalid")
            return jsonify({'message': 'invalid or not found token'}), 403
        else:
            return func(*args, **kwargs)
    return secure_func