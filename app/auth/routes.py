from flask import Flask, Blueprint, jsonify, request
from ..models.user import users

mod = Blueprint('auth', __name__)

users = [{"username": "mwalugha", "password": "mwalugha", "email" : "mwalughabura@gmai.com"}]

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

	user = {}
	user["username"] = "mwalugha"
	user["email"] = "mwalugha"
	user["password"] = "mwalugha"

	users.append(user)
	return jsonify(users)