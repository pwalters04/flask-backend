# app/admin/views.py

from flask import abort, flash, redirect, render_template, url_for
from flask_login import current_user, login_required

from . import admin
from forms import DepartmentForm, EmployeeAssignForm, RoleForm, AccountForm
from .. import db
from ..models import Department, Employee, Role, Account


def check_admin():
    """
    Prevent non-admins from accessing the page
    """
    if not current_user.is_admin:
        abort(403)


# Department Views


@admin.route('/departments', methods=['GET', 'POST'])
@login_required
def list_departments():
    """
    List all departments
    """
    check_admin()

    departments = Department.query.all()

    return render_template('admin/departments/departments.html',
                           departments=departments, title="Entries")


@admin.route('/departments/add', methods=['GET', 'POST'])
@login_required
def add_department():
    """
    Add a department to the database
    """
    check_admin()

    add_department = True

    form = DepartmentForm()
    if form.validate_on_submit():
        department = Department(name=form.name.data,
                                Normalside = form.Normalside.data,
                                AccCategory = form.AccCategory.data,
                                SaccCategory = form.SaccCategory.data,
                                iBalance = form.iBalance.data,
                                debit = form.debit.data,
                                credit = form.credit.data,
                                balance = form.balance.data,
                                Dtime = form.Dtime.data,
                                statement = form.statement.data,
                                Comment = form.Comment.data)
        try:
            # add department to the database
            db.session.add(department)
            db.session.commit()
            flash('You have successfully added a new entry.')
        except:
            # in case department name already exists
            flash('Error: entry name already exists.')

        # redirect to departments page
        return redirect(url_for('admin.list_departments'))

    # load department template
    return render_template('admin/departments/department.html', action="Add",
                           add_department=add_department, form=form,
                           title="Add Department")


@admin.route('/departments/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_department(id):
    """
    Edit an entry
    """
    check_admin()

    add_department = False

    department = Department.query.get_or_404(id)
    form = DepartmentForm(obj=department)
    if form.validate_on_submit():
        department.name = form.name.data
        department.Normalside = form.Normalside.data
        department.AccCategory = form.AccCategory.data
        department.SaccCategory = form.SaccCategory.data
        department.iBalance = form.iBalance.data
        department.debit = form.debit.data
        department.credit = form.credit.data
        department.balance = form.balance.data
        department.Dtime = form.Dtime.data
        department.statement =form.statement.data
        department.Comment = form.Comment.data
    
        
        db.session.commit()
        flash('You have successfully edited the entry.')

        # redirect to the departments page
        return redirect(url_for('admin.list_departments'))

    form.description.data = department.description
    form.name.data = department.name
    form.Normalside.data = department.Normalside
    form.AccCategory.data = department.AccCategory
    form.SaccCategory.data = department.SaccCategory
    form.iBalance.data = department.iBalance
    form.debit.data = department.debit
    form.credit.data = department.credit
    form.balance.data = department.balance
    form.Dtime.data = department.Dtime
    form.statement.data = department.statement
    form.Comment.data = department.Comment
    
    return render_template('admin/departments/department.html', action="Edit",
                           add_department=add_department, form=form,
                           department=department, title="Edit Entry")


@admin.route('/departments/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_department(id):
    """
    Delete a department from the database
    """
    check_admin()

    department = Department.query.get_or_404(id)
    db.session.delete(department)
    db.session.commit()
    flash('You have successfully deleted the entry.')

    # redirect to the departments page
    return redirect(url_for('admin.list_departments'))

    return render_template(title="Delete Department")
# Role Views


@admin.route('/roles')
@login_required
def list_roles():
    check_admin()
    """
    List all roles
    """
    roles = Role.query.all()
    return render_template('admin/roles/roles.html',
                           roles=roles, title='Roles')


@admin.route('/roles/add', methods=['GET', 'POST'])
@login_required
def add_role():
    """
    Add a role to the database
    """
    check_admin()

    add_role = True

    form = RoleForm()
    if form.validate_on_submit():
        role = Role(name=form.name.data,
                    description=form.description.data)

        try:
            # add role to the database
            db.session.add(role)
            db.session.commit()
            flash('You have successfully added a new role.')
        except:
            # in case role name already exists
            flash('Error: role name already exists.')

        # redirect to the roles page
        return redirect(url_for('admin.list_roles'))

    # load role template
    return render_template('admin/roles/role.html', add_role=add_role,
                           form=form, title='Add Role')


@admin.route('/roles/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_role(id):
    """
    Edit a role
    """
    check_admin()

    add_role = False

    role = Role.query.get_or_404(id)
    form = RoleForm(obj=role)
    if form.validate_on_submit():
        role.name = form.name.data
        role.description = form.description.data
        db.session.add(role)
        db.session.commit()
        flash('You have successfully edited the role.')

        # redirect to the roles page
        return redirect(url_for('admin.list_roles'))

    form.description.data = role.description
    form.name.data = role.name
    return render_template('admin/roles/role.html', add_role=add_role,
                           form=form, title="Edit Role")


@admin.route('/roles/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_role(id):
    """
    Delete a role from the database
    """
    check_admin()

    role = Role.query.get_or_404(id)
    db.session.delete(role)
    db.session.commit()
    flash('You have successfully deleted the role.')

    # redirect to the roles page
    return redirect(url_for('admin.list_roles'))

    return render_template(title="Delete Role")

# Employee Views

@admin.route('/employees')
@login_required
def list_employees():
    """
    List all employees
    """
    check_admin()

    employees = Employee.query.all()
    return render_template('admin/employees/employees.html',
                           employees=employees, title='Employees')


@admin.route('/employees/assign/<int:id>', methods=['GET', 'POST'])
@login_required
def assign_employee(id):
    """
    Assign a department and a role to an employee
    """
    check_admin()

    employee = Employee.query.get_or_404(id)

    # prevent admin from being assigned a department or role
    if employee.is_admin:
        abort(403)

    form = EmployeeAssignForm(obj=employee)
    if form.validate_on_submit():
        employee.role = form.role.data
        db.session.add(employee)
        db.session.commit()
        flash('You have successfully assigned a role.')

        # redirect to the roles page
        return redirect(url_for('admin.list_employees'))

    return render_template('admin/employees/employee.html',
                           employee=employee, form=form,
                           title='Assign Employee')


#Account Views
@admin.route('/accounts', methods=['GET', 'POST'])
@login_required
def list_account():
    """
    List all accounts
    """
    check_admin()

    accounts = Account.query.all()

    return render_template('admin/accounts/accounts.html',
                           accounts=accounts, title="accounts")


@admin.route('/accounts/add', methods=['GET', 'POST'])
@login_required
def add_account():
    """
    Add a account to the database
    """
    check_admin()

    add_account = True

    form = AccountForm()
    if form.validate_on_submit():
        account = Account(AccNum = form.AccNum.data,
                                name=form.name.data,
                                AccCategory = form.AccCategory.data,
                                SaccCategory = form.SaccCategory.data,
                                balance = form.balance.data,
                                Comment = form.Comment.data)
        try:
            # add department to the database
            db.session.add(account)
            db.session.commit()
            flash('You have successfully added a new entry.')
        except:
            # in case department name already exists
            flash('Error: entry name already exists.')

        # redirect to departments page
        return redirect(url_for('admin.list_account'))

    # load department template
    return render_template('admin/accounts/account.html', action="Add",
                           add_account=add_account, form=form,
                           title="Add Account")


@admin.route('/accounts/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_account(id):
    """
    Edit an entry
    """
    check_admin()

    add_account = False

    account = Account.query.get_or_404(id)
    form = AccountForm(obj=account)
    if form.validate_on_submit():
        account.AccNum = form.AccNum.data
        account.name = form.name.data
        account.AccCategory = form.AccCategory.data
        account.SaccCategory = form.SaccCategory.data
        account.balance = form.balance.data
        account.Comment = form.Comment.data
    
        
        db.session.commit()
        flash('You have successfully edited the entry.')

        # redirect to the departments page
        return redirect(url_for('admin.list_account'))
    form.AccNum.data = account.AccNum
    form.name.data = account.name
    form.AccCategory.data = account.AccCategory
    form.SaccCategory.data = account.SaccCategory
    form.balance.data = account.balance
    form.Comment.data = account.Comment
    
    return render_template('admin/accounts/account.html', action="Edit",
                           add_account=add_account, form=form,
                           account=account, title="Edit Entry")


@admin.route('/accounts/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_account(id):
    """
    Delete a department from the database
    """
    check_admin()

    account = Account.query.get_or_404(id)
    db.session.delete(account)
    db.session.commit()
    flash('You have successfully deleted the entry.')

    # redirect to the departments page
    return redirect(url_for('admin.list_account'))

    return render_template(title="Delete account")