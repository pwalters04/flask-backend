
# app/auth/__init__.py
from flask import Blueprint

admin = Blueprint('auth', __name__)


from . import views