from flask_restx import fields

def user_model(api):
    return api.model("User", {
        "username": fields.String(),
        "email": fields.String(),
        "first_name": fields.String(),
        "last_name": fields.String(),
        'created_at': fields.DateTime(dt_format='iso8601'),
        'updated_at': fields.DateTime(dt_format='iso8601'),
    })

def input_user_model(api):
    return api.model("InputUser", {
        "username": fields.String(),
        "email": fields.String(),
        "password": fields.String(),
        "first_name": fields.String(),
        "last_name": fields.String(),
    })

def user_login_model(api):
    return api.model("UserLogin", {
        "username": fields.String(),
        "password": fields.String(),
    })

def user_update_model(api):
    return api.model("UserUpdate", {
        "username": fields.String(),
        "first_name": fields.String(),
        "last_name": fields.String(),
    })