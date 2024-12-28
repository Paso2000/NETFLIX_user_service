from flask import Blueprint
from .users import users_bp
from .profiles import profiles_bp


def init_routes(app):
    app.register_blueprint(users_bp, url_prefix="/users", name="users_blueprint")
    app.register_blueprint(profiles_bp, url_prefix="/users", name="profiles_blueprint")
