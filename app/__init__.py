from flask import Flask
# from flask.ext.restful import Api, Resource

app = Flask(__name__)
# api = Api(app)

from app import routes

class User(object):
	"""docstring for User"""
	def __init__(self, name, password):
		self.name = name
		self.password = password

		return "User created."


# class UserAPI(Resource):
#     def get(self, id):
#         pass

#     def put(self, id):
#         pass

#     def delete(self, id):
#         pass

# api.add_resource(UserAPI, '/users/<int:id>', endpoint = 'user')