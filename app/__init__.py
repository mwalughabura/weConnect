from flask import Flask

app = Flask(__name__)

from app import routes

class User(object):
	"""docstring for User"""
	def __init__(self, name, password):
		self.name = name
		self.password = password

		return "User created."