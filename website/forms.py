# Creates forms for user to fill out on webpage

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from website.models import Volunteer

# Form for checking if email is eligible for registering in events
class RegisterForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Register')

# Form for adding volunteer emails that are eligible for events (testing purposes)
class AddVolunteerForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Add Volunteer')