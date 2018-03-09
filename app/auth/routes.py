from flask import Flask, Blueprint, jsonify, request
from ..models.user import users
from ..models.user import User

mod = Blueprint('auth', __name__)

users = [{"mwalugha" : ["mwalugha", "mwalughabura@gmail.com", "mwalugha"]}]
logs = []
user_instance = User()


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
	# username = users["username"]
	cu = user_instance.create_user(users[0]["mwalugha"][0], users[0]["mwalugha"][1], users[0]["mwalugha"][2], users[0]["mwalugha"][2])
	
	if cu == "User has been successfully created.":
		users.append(user)	
		return jsonify(users)
	return jsonify(cu)