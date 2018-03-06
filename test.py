from flask import Flask
from flask_testing import TestCase

class MyTest(TestCase):

	def create_app(self):

		app = Flask(__name__)
		app.config['TESTING'] = True
		return app

	def test_create_user(self):

		user = User(name, password)
		assertTrue(len(self.name) > 1, "User created.") and assertTrue(len(self.password) > 1, "User created.")