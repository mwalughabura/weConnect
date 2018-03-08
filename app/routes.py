from app import app
from app.models.user import User
# from flask.ext.login import login_required


# protected route
@app.route('/secret', methods = ['GET', 'POST'])
# @login_required
def secret():
	return 'Only authenticated users are allowed!'


@app.route('/')
def index():
    return "Hello, Mwalugha!"

# registration route
@app.route('/registration', methods = ['POST'])
def registration():

	return "You have successfully signed up."


# login route
@app.route('/login', methods = ['POST'])
def login():

	return "You have successfully logged in."