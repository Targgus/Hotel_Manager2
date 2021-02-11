# from app import db 
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Guest(db.Model):
    __tablename__ = 'guests'
    id = db.Column(db.Integer, primary_key = True, unique=True)
    firstName = db.Column(db.String(100))
    lastName = db.Column(db.String(100))
    roomNumber = db.Column(db.Integer)

    def __init__(self, firstName, lastName, roomNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.roomNumber = roomNumber