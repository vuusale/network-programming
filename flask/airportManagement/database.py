from flask_sqlalchemy import SQLAlchemy
from main import app
import json

db = SQLAlchemy(app)

class Admin(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), nullable=False, unique=True)
    password = db.Column(db.String(64), nullable=False)

    def __repr__(self):
        return f"Admin(user_id: {self.user_id}, username: {self.username})"

class Flight(db.Model):
    flight_id = db.Column(db.Integer, primary_key=True)
    from_city = db.Column(db.String(100), nullable=False)
    to_city = db.Column(db.String(100), nullable=False)
    departure_date = db.Column(db.String(10), nullable=False)
    arrival_date = db.Column(db.String(16), nullable=False)
    passenger_num = db.Column(db.Integer, nullable=False)
    airplane_info = db.Column(db.String(64))

    def __repr__(self):
        return f"Flight(flight_id: {self.flight_id}, from: {self.from_city}, to: {self.to_city})"

if __name__ == "__main__":
    db.create_all()
    with open("logins.json", "r") as f:
        jsonfile = f.read()
        logins = json.loads(jsonfile)
        for username, password in logins.items():
            admin = Admin(username=username, password=password)
            db.session.add(admin)
    with open("flights.json", "r") as f:
        jsonfile = f.read()
        flights = json.loads(jsonfile)
        for flight in flights:
            flight = Flight(**flight)
            db.session.add(flight)
    db.session.commit()