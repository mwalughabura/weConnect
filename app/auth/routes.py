from flask import Blueprint

mod = Blueprint('auth', __name__)

@mod.route('/login', methods=['GET', 'POST'])
def login():
	return "Yes you have logged in."

@mod.route('/logout', methods=['GET', 'POST'])
def logout():
	return "Yes you have been logged out."

@mod.route('/register', methods=['GET', 'POST'])
def register():
	return "Yes you have registered."