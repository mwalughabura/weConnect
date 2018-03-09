from flask import Flask, Blueprint, jsonify, request
from ..models.user import users

mod = Blueprint('auth', __name__)

users = [{"username": "mwalugha", "password": "mwalugha", "email" : "mwalughabura@gmai.com", "logged_in" : False}]
logs = []


# log in endpoints
@mod.route('/login', methods=['POST'])
def login():
	login = {}
	login["username_or_email"] = "mwalugha"
	login["password"] = "mwalugha"
	login["logged_in"] = True

	logs.append(login)
	return jsonify(logs)

# log out endpoints
@mod.route('/logout', methods=['POST'])
def logout():
	logout = {}
	logout["username_or_email"] = "mwalugha"
	logout["logged_in"] = False

	logs.append(logout)
	return jsonify(logs)


# register endpoints
@mod.route('/register', methods=['POST'])
def register():

	user = {}
	user["username"] = "mwalugha"
	user["email"] = "mwalugha"
	user["password"] = "mwalugha"

	users.append(user)
	return jsonify(users)