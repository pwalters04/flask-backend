# app/admin/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DecimalField, SelectField, DateTimeField, IntegerField
from wtforms.validators import DataRequired
import decimal
import datetime
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from ..models import Role


class DepartmentForm(FlaskForm):
    """
    Form for admin to add or edit a department
    """
   
    
    name = StringField('Accountant Name', validators=[DataRequired()])
    description = StringField('Accountant description', validators=[DataRequired()])
    Normalside = SelectField('Normal side', choices = [('Right','Right'),('Left','Left')])
    AccCategory = SelectField('Account catergory', choices = [('asset','asset'),('liability','liability'),('expense','expense'),('revenue','revenue'),('equity','equity')])
    SaccCategory = SelectField('Sub-Category', choices = [('Accounts Payable','Accounts Payable'),('Accounts Recieveable','Accounts Recieveable'),('Cash','Cash'),('Interest on loan','Interest on loan')])
    iBalance = DecimalField ('Initital balance', places= 2,validators=[DataRequired()])
    debit = DecimalField ('debit', places= 2,validators=[DataRequired()])
    credit = DecimalField ('Credit', places= 2,validators=[DataRequired()])
    balance = DecimalField ('Balance', places= 2,)
    Dtime = DateTimeField ('time posted(EDT)',format ='%Y-%m-%d %H:%M:%S',default= datetime.datetime.now())
    #employeeiD
    #orderiD
    statement = SelectField('Statement', choices = [('IS','Income Statement'),('BS','Balance sheet'),('RE','Retained earnings statement')])
    Comment = StringField('Comment', validators=[DataRequired()])


    submit = SubmitField('Submit')

    #StringField('', validators=[DataRequired])

class RoleForm(FlaskForm):
    """
    Form for admin to add or edit a role
    """
    name = StringField('Name', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Submit')

class EmployeeAssignForm(FlaskForm):
    """
    Form for admin to assign departments and roles to employees
    """
    role = QuerySelectField(query_factory=lambda: Role.query.all(),
                            get_label="name")
    submit = SubmitField('Submit')

class AccountForm(FlaskForm):
    """
    Form for admin to add or edit a department
    """
   
    AccNum = IntegerField('Account Number', validators=[DataRequired()])
    name = StringField('Account Name', validators=[DataRequired()])
    #description = StringField('Account description', validators=[DataRequired()])
    #Normalside = SelectField('Normal side', choices = [('Right','Right'),('Left','Left')])
    AccCategory = SelectField('Account catergory', choices = [('asset','asset'),('liability','liability'),('expense','expense'),('revenue','revenue'),('equity','equity')])
    SaccCategory = SelectField('Sub-Category', choices = [('Current','Current'),('Long-term','Long-term')])
    #iBalance = DecimalField ('Initital balance', places= 2,validators=[DataRequired()])
    #debit = DecimalField ('debit', places= 2,validators=[DataRequired()])
    #credit = DecimalField ('Credit', places= 2,validators=[DataRequired()])
    balance = DecimalField ('Balance', places= 2,)
    #Dtime = DateTimeField ('time posted(EDT)',format ='%Y-%m-%d %H:%M:%S',default= datetime.datetime.now())
    #employeeiD
    #orderiD
    #statement = SelectField('Statement', choices = [('IS','Income Statement'),('BS','Balance sheet'),('RE','Retained earnings statement')])
    Comment = StringField('Comment', validators=[DataRequired()])
    

    submit = SubmitField('Submit')

    #StringField('', validators=[DataRequired])