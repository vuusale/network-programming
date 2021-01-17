from flask_restful import reqparse

flight_post_args = reqparse.RequestParser()
flight_post_args.add_argument("from_city", type=str, required=True, help="From city")
flight_post_args.add_argument("to_city", type=str, required=True, help="To city")
flight_post_args.add_argument("departure_date", type=str, required=True, help="Departure date")
flight_post_args.add_argument("arrival_date", type=str, required=True, help="Arrival date")
flight_post_args.add_argument("passenger_num", type=int, required=True, help="Number of passengers")
flight_post_args.add_argument("airplane_info", type=str, help="Airplane information")
flight_post_args.add_argument("token", type=str, help="Authorization token")

flight_put_args = reqparse.RequestParser()
flight_put_args.add_argument("flight_id", type=int, required=True, help="Flight id")
flight_put_args.add_argument("to_city", type=str, help="To city")
flight_put_args.add_argument("departure_date", type=str, help="Departure date")
flight_put_args.add_argument("arrival_date", type=str, help="Arrival date")
flight_put_args.add_argument("passenger_num", type=int, help="Number of passengers")
flight_put_args.add_argument("airplane_info", type=str, help="Airplane information")
flight_put_args.add_argument("token", type=str, help="Authorization token")

flight_delete_args = reqparse.RequestParser()
flight_delete_args.add_argument("flight_id", type=str, required=True, help="Flight id")
flight_delete_args.add_argument("token", type=str, help="Authorization token")

auth_login_args = reqparse.RequestParser()
auth_login_args.add_argument("username", type=str, required=True, help="Username")
auth_login_args.add_argument("password", type=str, required=True, help="Password")

auth_logout_args = reqparse.RequestParser()
auth_logout_args.add_argument("token", type=str, required=True, help="Authorization token")