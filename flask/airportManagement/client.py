import requests
import json

HOST = "http://127.0.0.1:5000"

if __name__ == "__main__":
    while True:
        try:
            command = input("Method route: ").split()
            if command[0] == "exit":
                print("Good bye!")
                break
            else:
                method = command[0]
                route = command[1]
                if method.lower() == "get":
                    res = requests.get(f"{HOST}/{route}")
                    print(res.json())
                elif method.lower() == "post":
                    if route == "authentication_authorization":
                        username = input("Username: ")
                        password = input("Password: ")
                        token = requests.post(f"{HOST}/authentication_authorization", data={
                            "username": username,
                            "password": password
                        }).json()
                        print(f"Token: {token['token']}")
                    elif route == "end_session":
                        token = input("Token: ")
                        res = requests.post(f"{HOST}/end_session", data={"token": token})
                        print(res.json())
                    elif route == "flights":
                        from_city = input("From: ")
                        to_city = input("To: ")
                        departure_date = input("Departure date: ")
                        arrival_date = input("Arrival date: ")
                        passenger_num = input("Number of passengers: ")
                        airplane_info = input("Airplane info: ")
                        token = input("Token: ")
                        res = requests.post(f"{HOST}/flights", data={
                            "from_city": from_city if from_city else None,
                            "to_city": to_city if to_city else None,
                            "departure_date": departure_date if departure_date else None,
                            "arrival_date": arrival_date if arrival_date else None,
                            "passenger_num": int(passenger_num) if passenger_num else None,
                            "airplane_info": airplane_info if airplane_info else None,
                            "token": token
                        })
                        print(res.json())
                    else:
                        print("Invalid post route")
                elif method.lower() == "delete":
                    flight_id = int(input("Flight id: "))
                    token = input("Token: ")
                    res = requests.delete(f"{HOST}/flights", data={
                        "flight_id": flight_id,
                        "token": token
                    })
                    print(res.status_code)
                elif method.lower() == "put":
                    flight_id = int(input("Flight id: "))
                    from_city = input("From: ")
                    to_city = input("To: ")
                    departure_date = input("Departure date: ")
                    arrival_date = input("Arrival date: ")
                    passenger_num = input("Number of passengers: ")
                    airplane_info = input("Airplane info: ")
                    token = input("Token: ")
                    data = {
                        "flight_id": flight_id,
                        "from_city": from_city if from_city else None,
                        "to_city": to_city if to_city else None,
                        "departure_date": departure_date if departure_date else None,
                        "arrival_date": arrival_date if arrival_date else None,
                        "passenger_num": int(passenger_num) if passenger_num else None,
                        "airplane_info": airplane_info if airplane_info else None,
                        "token": token
                    }
                    res = requests.put(f"{HOST}/flights", data=data)
                    print(res.json())
                else:
                    print("Invalid method")
        except (IndexError, ValueError) as e:
            print(e)
            print("Invalid input")
        except json.decoder.JSONDecodeError:
            print("Invalid route")
