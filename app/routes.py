from app import app

@app.route('/')
def index():
    return "Hello, Mwalugha!"

# login route
@app.route('/api/auth/login')
def login():
	return "You have successfully logged in."

# register route
@app.route('/api/auth/register')
def login():
	return "You have successfully registered."

# log out route
@app.route('/api/auth/logout')
def login():
	return "You have logged out."

# reset password route
@app.route('/api/auth/reset-password')
def login():
	return "Your password has been reset."