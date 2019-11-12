# app/admin/views.py

from flask import abort, flash, redirect, render_template, url_for
from flask_login import current_user, login_required

from . import admin
from forms import DepartmentForm
from .. import db
from ..models import Department


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
                           departments=departments, title="Departments")


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
                                description=form.description.data,
                                Normalside = form.Normalside.data,
                                AccCategory = form.AccCategory.data,
                                SaccCategory = form.SaccCategory.data,
                                iBalance = form.iBalance.data)
        try:
            # add department to the database
            db.session.add(department)
            db.session.commit()
            flash('You have successfully added a new department.')
        except:
            # in case department name already exists
            flash('Error: department name already exists.')

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
        department.description = form.description.data
        department.Normalside = form.Normalside.data
        department.AccCategory = form.AccCategory.data
        department.SaccCategory = form.SaccCategory.data
        department.iBalance = form.iBalance.data
    
        
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