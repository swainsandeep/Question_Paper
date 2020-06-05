from flask import render_template,flash,redirect,url_for,jsonify
from flask_wtf import FlaskForm
from wtforms import SubmitField
from codeblog.model import EmployeeDetails
from codeblog import app,db


@app.route("/",methods =['GET','POST'])
def welcome():
    data_list = EmployeeDetails.query.all()
    if data_list:
        return render_template('view_data.html',title='view_data',data_list=data_list)
    else:
        flash(f'No Data found','danger')
        return render_template('view_data.html',title='view_data',data_list=data_list)


@app.route("/add_data",methods =['GET','POST'])
def add_data():

    class CreateEmployee(FlaskForm):
        submit = SubmitField('Add Records')

    form = CreateEmployee()
    if form.validate_on_submit():
        for i in range(10):
            employee_name = 'sandeep'+str(i)
            employee_details = EmployeeDetails(employee_name=employee_name)
            db.session.add(employee_details)
            db.session.commit()
        
        return redirect(url_for('welcome'))


    return render_template ('add_data.html',form = form)