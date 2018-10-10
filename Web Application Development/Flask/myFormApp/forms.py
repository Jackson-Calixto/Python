





from flask_wtf import Form
from wtforms import TextField, RadioField, IntegerField, TextAreaField, SelectField, SubmitField

from wtforms import validators

class ContactForm(Form):
    name = TextField("Name", [validators.Required("You must fill your name.")])
    gender = RadioField("Gender", choices = [('M', 'Male'), ('F', 'Female')])

    age = IntegerField("Age")

    email = TextField("Email", [validators.Required("You must enter an email address."), validators.Email("Please enter a valid email address.")])


    message = TextAreaField("Message")

    language = SelectField('Preferred Language', choices = [('en', 'English'), ('es', 'Spanish'), ('fr', 'French')])

    submit = SubmitField("Submit")
