




from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from forms import CarForm

# Create WSGI application object
app = Flask(__name__)

# Specify secret key to use CSRF prevention in the form
app.secret_key = 'jnkmdwklqn!@'

# Set database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vehicles.sqlite3'

# Track modifications of objects and emit signals
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# SQLAlchemy object contains helper functions for ORM operations
db = SQLAlchemy(app)

""" Database model class """
class cars(db.Model):
    # Specify table fields
    id = db.Column('car_id', db.Integer, primary_key = True)
    make = db.Column(db.String(50))
    model = db.Column(db.String(50))
    year = db.Column(db.Integer)
    transmission = db.Column(db.String(10))

    # Initializes data model
    def __init__(self, make, model, year, transmission):
        self.make = make
        self.model = model
        self.year = year
        self.transmission = transmission

""" Retrieves and displays all car records from the database table """
@app.route('/showcars')
def show_cars():
    # Call up the template to display all cars
    return render_template('showcars.html', cars = cars.query.all())

""" Renders form for adding new cars to the database table """
@app.route('/addcar', methods = ['GET', 'POST'])
def add_car():
    # Create new car form object
    form = CarForm()
    if request.method == 'POST':
        # Form submitted with empty fields and/or erroneous input
        if form.validate() == False:
            # Abort submission, show validation error messages, and re-display from with filled fields
            return render_template('addcar.html', form = form)
        else:
            # Create new car object from data in each form input field
            car = cars(request.form['make'],
                       request.form['model'],
                       request.form['year'],
                       request.form['transmission']
                       )
            # Insert new car record into mapped table
            db.session.add(car)
            # Save changes to data
            db.session.commit()
            # Flash a message confirming successful data entry on cars list page
            flash('New car record successfully added')
            return redirect(url_for('show_cars'))
    elif request.method == 'GET':
        # Display empty form using form template
        return render_template('addcar.html', form = form)

if __name__ == '__main__':
    # Create database tables and run the WSGI application on port 8010
    db.create_all()
    app.run(port = 8010)
