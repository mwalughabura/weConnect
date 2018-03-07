from app import app
# from flask.ext.login import login_required


# protected route
@app.route('/secret')
# @login_required
def secret():
	return 'Only authenticated users are allowed!'


@app.route('/')
def index():
    return "Hello, Mwalugha!"

# login route
@app.route('/api/auth/login', methods = ['GET', 'POST'])
def login():
	return "You have successfully logged in."