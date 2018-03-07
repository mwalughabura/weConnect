from flask import Blueprint

mod = Blueprint('auth', __name__)

@mod.route('/login', methods=['GET', 'POST'])
def login():
	return "Yes you have logged in."