# app/admin/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DecimalField
from wtforms.validators import DataRequired


class DepartmentForm(FlaskForm):
    """
    Form for admin to add or edit a department
    """
    name = StringField('Accountant name', validators=[DataRequired()])
    description = StringField('Accountant description', validators=[DataRequired()])
    #normal side
    #Account catergory
    #Account sub-catergory
    #initial balance
    #debit
    #credit
    #balance
    #date/time added
    #user id
    #order
    #Statement
    #Comment

    amount = DecimalField('Amount', validators=[DataRequired()])
    submit = SubmitField('Submit')