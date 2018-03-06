from flask import Flask
from flask_testing import TestCase
from app.models import login

class MyTest(TestCase):

	def create_app(self):

		app = Flask(__name__)
		app.config['TESTING'] = True
		return app

	def test_create_user(self):

		user = User(name, password)
		assertTrue(len(self.name) > 1 and len(self.password) > 1, "User created.")

	def test_login(self):
		response = self.get('/app/models/login')
		self.assertIn('Please login', response.users)

	
	def test_signout(self):
		response = self.get('/app/models/logout')
		self.assertIn('You are logged out.', response)