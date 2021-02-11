import configparser

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from models import Guest, db


app = Flask(__name__, template_folder='templates')

config = configparser.ConfigParser()
config.read('./config.ini')

ENV = 'prod'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://postgres:{config['dev_db']['password']}@localhost:{config['dev_db']['port']}/hotel_manager"
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = f"{config['prod_db']['postgresURL']}"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)
db.init_app(app)

# basic route
@app.route('/')
def index():
    # renders index.html and queries Guest table from sqlite and displays all guests
    return render_template('index.html', guests=Guest.query.all())

# route for form submission
@app.route("/submit", methods=['POST'])
def submit():
    if request.method == "POST":
        # grabs form data
        firstName = request.form['guestFirstName']
        lastName = request.form['guestLastName']
        roomNumber = request.form['roomNumber']

        # checks if firstname exists
        if firstName:
            # creates existing_user variable based on information within the database
            existing_user = Guest.query.filter(Guest.firstName == firstName).first()
        # checks is roomnumber exists
        if roomNumber:
            # creates existing_room variable based on information within the database
            existing_room = Guest.query.filter(Guest.roomNumber == roomNumber).first()
        # if existing user and existing room exist, send message back to index and do not allow database submission
        if existing_user:
            return render_template('index.html', guests=Guest.query.all(), message='They are already checked in')
        if existing_room:
            return render_template('index.html', guests=Guest.query.all(), message='That room is currently booked')

        # build variable that holds Guest object filled in with form data
        data = Guest(firstName=firstName, lastName=lastName, roomNumber=roomNumber)

        # add data variable to database
        db.session.add(data)
        # commit data
        db.session.commit()
    # render index will all guests from database
    return render_template('index.html', guests=Guest.query.all())

@app.route("/delete/<int:guestid>", methods=['GET', 'POST'])
def delete(guestid):
    print(guestid)
    Guest.query.filter(Guest.id==guestid).delete()
    db.session.commit()
    return render_template('index.html', guests=Guest.query.all())


if __name__ == '__main__':
    app.run()