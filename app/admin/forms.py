# app/admin/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DecimalField
from wtforms.validators import DataRequired
import decimal


class DepartmentForm(FlaskForm):
    """
    Form for admin to add or edit a department
    """
    name = StringField('Accountant name', validators=[DataRequired()])
    description = StringField('Accountant description', validators=[DataRequired()])
    Normalside = StringField('Normal Side', validators=[DataRequired()])
    AccCategory = StringField('Account category', validators=[DataRequired()])
    SaccCategory = StringField('Sub-Account category', validators=[DataRequired()])
    iBalance = DecimalField ('Initital balance', places= 2,validators=[DataRequired()])
    debit = DecimalField ('debit', places= 2,validators=[DataRequired()])
    #credit
    #balance
    #Dtime
    #employeeiD
    #OrderiD
    #Statement
    #Comment


    submit = SubmitField('Submit')

    #StringField('', validators=[DataRequired])