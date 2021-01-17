from flask import request
from flask_restful import Api, Resource, reqparse, marshal_with, fields, abort
from flask_sqlalchemy import SQLAlchemy
from random import randint

from main import app
from database import db, Admin, Flight
from args import flight_post_args, flight_put_args, flight_delete_args, auth_login_args, auth_logout_args

api = Api(app)

flight_fields = {
    "flight_id": fields.Integer,
    "from_city": fields.String,
    "to_city": fields.String,
    "departure_date": fields.String,
    "arrival_date": fields.String,
    "passenger_num": fields.Integer,
    "airplane_info": fields.String
}

sessions = {}

class Flights(Resource):
    @marshal_with(flight_fields)
    def get(self, from_city, to_city):
        if from_city == "null":
            if to_city == "null":
                flights = Flight.query.filter_by().all()
            else:
                flights = Flight.query.filter_by(to_city=to_city).all()
        elif to_city == "null":
            flights = Flight.query.filter_by(from_city=from_city).all()
        else:
            flights = Flight.query.filter_by(from_city=from_city, to_city=to_city).all()
        return flights, 200

class FlightAdmin(Resource):
    @marshal_with(flight_fields)
    def post(self):
        args = flight_post_args.parse_args()
        if args.token not in sessions.values():
            abort(401, message="Not authorized for this operation")

        del args["token"]
        flight = Flight(**args)
        db.session.add(flight)
        db.session.commit()
        return flight, 201

    def delete(self):
        args = flight_delete_args.parse_args()
        if args.token not in sessions.values():
            abort(401, message="Not authorized for this operation")

        flight = Flight.query.filter_by(
            flight_id=args.flight_id)
        if not flight.first():
            abort(404, message="No such flight")

        flight.delete()
        db.session.commit()
        return "", 204

    @marshal_with(flight_fields)
    def put(self):
        args = flight_put_args.parse_args()
        if args.token not in sessions.values():
            abort(401, message="Not authorized for this operation")

        flight = Flight.query.filter_by(
            flight_id=args.flight_id).first()
        if not flight:
            abort(404, message="No such flight")
        for key, value in args.items():
            if value and key != "token" and key != "flight_id":
                setattr(flight, key, value)
        db.session.commit()
        return flight, 200

class Auth(Resource):
    def post(self):
        args = auth_login_args.parse_args()
        user = Admin.query.filter_by(username=args.username, password=args.password).first()
        if not user:
            abort(400, message="Invalid username or password")
        
        token = str(randint(1000000, 10000000))
        sessions[args.username] = token
        return {"token": token}, 200

class Logout(Resource):
    def post(self):
        args = auth_logout_args.parse_args()
        token = args.token
        if token not in sessions.values():
            abort(404, message="No such session")

        for key, value in sessions.copy().items():
            if value == token:
                del sessions[key]
        return {"message": "Logged out successfully"}, 200

api.add_resource(FlightAdmin, "/flights")
api.add_resource(Flights, "/flights/<string:from_city>/<string:to_city>")
api.add_resource(Auth, "/authentication_authorization")
api.add_resource(Logout, "/end_session")

if __name__ == "__main__":
    app.run(debug=True)