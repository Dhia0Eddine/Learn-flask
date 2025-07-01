# Role: Defines the structure of your database tables using SQLAlchemy ORM. This file maps Python classes to actual database tables.
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Venue(db.Model):
    __tablename__='venues'

    id = db.Column(db.Integer, primary_key=True)              # Unique ID
    name = db.Column(db.String(100), nullable=False)          # Venue name (required)
    location = db.Column(db.String(100), nullable=True)       # Optional location
    capacity = db.Column(db.Integer, nullable=True)           # Optional capacity

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "location": self.location,
            "capacity": self.capacity
        }
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(128), nullable=False)
    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email
        }