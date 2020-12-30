# Methods managing how each webpage operates

from flask import render_template, url_for, flash, redirect, request
from website import app, db
from website.forms import RegisterForm, AddVolunteerForm # import forms from forms.py
from website.models import Volunteer, Entry

# from flask_login import login_user, current_user, logout_user, login_required

@app.route("/add-volunteer", methods=['GET', 'POST'])
def add_volunteer():
    form = AddVolunteerForm() # Displays volunteer form

    if form.validate_on_submit():
        # Creates Volunteer object
        volunteer = Volunteer(email=form.email.data)

        # Adds email to database of eligible emails
        db.session.add(volunteer)
        db.session.commit()

        # Displays confirmation message
        flash('Email address ' + form.email.data + ' is now eligible for event registration.')
    
    return render_template('add_volunteer.html', title='Add Volunteer', form=form)

@app.route("/", methods=['GET', 'POST'])
@app.route("/home",methods=['GET', 'POST'])
def home():
    return render_template('home.html')
@app.route("/aboutus",methods=['GET', 'POST'])
def aboutus():
    return render_template('aboutus.html')
@app.route("/contact",methods=['GET', 'POST'])
def contact():
    return render_template('contact.html')
@app.route("/getinvolved",methods=['GET', 'POST'])
def getinvolved():
    return render_template('getinvolved.html')

@app.route("/events", methods=['GET', 'POST'])
def check_eligibility():
    form = RegisterForm()

    # if form.validate_on_submit():
    if form.is_submitted():
        # Checks if volunteer object has matching email
        email = Volunteer.query.filter_by(email=form.email.data).first()

        # Displays confirmation message
        if email:
            flash('You are eligible to register for this event.', 'Success')

        else:
            invalid_email = Entry.query.filter_by(email=form.email.data).first()
            
            # Adds email to database if not already in database
            if not invalid_email:
                new_email = Entry(email=form.email.data)
                db.session.add(new_email)
                db.session.commit()

            # Displays error message
            flash('You are not eligible for event registration. Please complete training and come back later.', 'Email Invalid')

    
    return render_template('events.html')
