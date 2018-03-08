from flask import Blueprint, jsonify, request
from ..models.user import users

mod = Blueprint('auth', __name__)

# this is just for testing
@mod.route('/test', methods=['GET'])
def test():
	return jsonify({"key": "value"})


@mod.route('/login', methods=['POST'])
def login():
	return "Yes you have logged in."

@mod.route('/logout', methods=['POST'])
def logout():
	return "Yes you have been logged out."

@mod.route('/register', methods=['POST'])
def register():
	username = request.json['username']
	return jsonify({username})
	# appended = {"username": "mwalugha"}

	# users.append(appended)
	# return jsonify(appended)