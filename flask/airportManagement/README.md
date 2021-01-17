# Airport Management
 
This is the repository of mini airport management application built with Flask Restful and SQLite.

![Screenshot of running client.py](https://github.com/vuusale/airport_management/blob/main/client.png)

## Prerequisites
It is required to have Python3 installed in order to run the application. Just go to the [official Python website](https://python.org/) and download the release suitable to your machine. For example, if you have 64-bit Windows operating system, download *Windows x86-64 executable installer*. 

After ensuring that Python3 is set up, follow the below steps:

- Clone the repository into a desired location:
  
      $ git clone https://github.com/vuusale/airport_management.git
      
- Install the requirements:
  
      $ pip install -r requirements.txt
  
Now you are ready to run the program. 

## Usage
Open 2 terminals and run the following command on the first one to start the server:

    $ python3 server.py
    
On the second pane, run the following in order to create the database:

    $ python3 database.py
    
To use the services interactively, run the following command on the same window:
    
    $ python3 client.py
    
Now, follow the prompts and make HTTP requests:

###### GET
    Method route: get flights/<from_city>/<to_city>
If `from_city` is null, flights to `to_city` are returned.<br>
If `to_city` is null, flights from `from_city` are returned.<br>
If both `from_city` and to_city are null, all flights are returned.
###### POST
    Method route: post authentication_authorization
    Method route: post end_session
    Method route: post flights
###### DELETE
    Method route: delete flights
###### PUT
    Method route: put flights

## Task
The task is to create a client-server-based “Airport Management” RESTful API with two roles: admin and client.

Admin – user that has ability to get, post, update and delete flight data<br>
Client – user that has ability to get the data

###### For Admin
<ul>
  <li>Localhost/authentication_authorization - to login using username and password</li>
  <li>Localhost/flights - to add, delete, and update the flights</li>
  <li>Localhost/flights/from/to - get the list of flights from – city, to - city</li>
  <li>Localhost/end_session – to end the session</li>
</ul>

###### For User
<ul>
  <li>Localhost/flights/from/to - get the list of flights from – city, to - city</li>
</ul>