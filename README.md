# Flask Webcast on Circular Dependencies

This is the example code featured in my webcast on Circular Dependencies in Python and Flask, available at https://www.youtube.com/watch?v=NH-8oLHUyDc. The application is based on the code from my blog article on SQLAlchemy soft deletes: http://blog.miguelgrinberg.com/post/implementing-the-soft-delete-pattern-with-flask-and-sqlalchemy.

## How to Run

- Create a virtual environment and activate it (Python 2.7 and Python 3.4+ are both okay)
- Install the requirements: `pip install -r requirements.txt`
- Create the database: `flask db upgrade`
- Run the service: `flask run`

## How to Use

This example implements a small API that can be accessed from the command line. The httpie client is installed and you can use it to send requests. Below are some example commands:

To create a new user with name "john":

    http POST http://localhost:5000/users name=john

To get the list of users:

    http GET http://localhost:5000/users

To get the user with id 1:

    http GET http://localhost:5000/users/1

To add a message from the user with id 2:

    http POST http://localhost:5000/users/2/messages message=hello

To get the list of messages:

    http GET http://localhost:5000/messages

To delete the user with id 3:

    http DELETE http://localhost:5000/users/3
