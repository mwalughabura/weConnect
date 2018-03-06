from app import app

@app.route('/')
def index():
    return "Hello, Mwalugha!"

# login route
@app.route('/api/auth/login', methods = ['POST'])
def login():
	return "You have successfully logged in."

# register route
@app.route('/api/auth/register', methods = ['POST'])
def login():
	return "You have successfully registered."

# log out route
@app.route('/api/auth/logout', methods = ['POST'])
def login():
	return "You have logged out."

# reset password route
@app.route('/api/auth/reset-password', methods = ['POST'])
def login():
	return "Your password has been reset."

