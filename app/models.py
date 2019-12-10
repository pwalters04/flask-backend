from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login_manager
import datetime

class Employee(UserMixin, db.Model):
    """
    Create an Employee table
    """

    # Ensures table will be named in plural and not in singular
    # as is the name of the model
    __tablename__ = 'employees'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), index=True, unique=True)
    username = db.Column(db.String(60), index=True, unique=True)
    first_name = db.Column(db.String(60), index=True)
    last_name = db.Column(db.String(60), index=True)
    password_hash = db.Column(db.String(128))
    department_id = db.Column(db.Integer, db.ForeignKey('departments.id'))
    account_id = db.Column(db.Integer, db.ForeignKey('accounts.id'))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    is_admin = db.Column(db.Boolean, default=False)

    @property
    def password(self):
        """
        Prevent pasword from being accessed
        """
        raise AttributeError('password is not a readable attribute.')

    @password.setter
    def password(self, password):
        """
        Set password to a hashed password
        """
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        """
        Check if hashed password matches actual password
        """
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<Employee: {}>'.format(self.username)


# Set up user_loader
@login_manager.user_loader
def load_user(user_id):
    return Employee.query.get(int(user_id))


class Department(db.Model):
    """
    Create a Department table
    """

    __tablename__ = 'departments'

    id = db.Column(db.Integer, primary_key=True)
    accNum = db.Column(db.Integer, unique=True)
    name = db.Column(db.String(60), unique=True)
    #description = db.Column(db.String(200))
    #Normalside = db.Column(db.String(5))
    AccCategory = db.Column(db.String(25))
    #SaccCategory = db.Column(db.String(25))
    #iBalance = db.Column(db.Numeric(8,2))
    #debit = db.Column(db.Numeric(8,2))
    #credit = db.Column(db.Numeric(8,2))
    balance = db.Column(db.Numeric(8,2))
    Dtime = db.Column(db.DateTime(),default=datetime.datetime.now())
    #statement = db.Column(db.String(25))
    Comment = db.Column(db.String(60))
    employees = db.relationship('Employee', backref='department',
                                lazy='dynamic')

    def __repr__(self):
        return '<Department: {}>'.format(self.name)


class Role(db.Model):
    """
    Create a Role table
    """

    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True)
    description = db.Column(db.String(200))
    employees = db.relationship('Employee', backref='role',
                                lazy='dynamic')

    def __repr__(self):
        return '<Role: {}>'.format(self.name)
    
class Account(db.Model):
    """
    Create a Account table
    """

    __tablename__ = 'accounts'

    id = db.Column(db.Integer, primary_key=True)
    AccNum = db.Column(db.Integer())
    name = db.Column(db.String(60), unique=True)
    AccCategory = db.Column(db.String(25))
    SaccCategory = db.Column(db.String(25))
    balance = db.Column(db.Numeric(8,2))
    Comment = db.Column(db.String(60))
    employees = db.relationship('Employee', backref='account',
                                lazy='dynamic')

    def __repr__(self):
        return '<Account: {}>'.format(self.name)