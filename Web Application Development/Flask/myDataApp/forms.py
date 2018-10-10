





from flask_wtf import Form
from wtforms import TextField, IntegerField, SelectField, SubmitField

from wtforms import validators

class CarForm(Form):
    make = TextField("Make",
                     [validators.Required("You must specify a valid vehicle make.")
                     ])

    model = TextField("Model",
                      [validators.Required("You must specify a valid model.")
                      ])

    year = IntegerField("Year",
                        [validators.Required("You must specify a valid year."),
                         validators.NumberRange(min=1980,
                                                max=2017,
                                                message="Year must be between 1980 and 2017")
                         ])

    transmission = SelectField('Transmission Type',
                               choices = [('Manual', 'Manual'),
                                          ('Automatic', 'Automatic')
                                          ])

    submit = SubmitField("Submit")
