import unittest
from ..models.user import User


#from ..app.models.user import User

class UserModelTestCase(unittest.TestCase):
	def setUp(self):
		self.user = User()

	def test_create_user(self):
		response = self.user.create_user("John", "john@gmail.com", "randomname", "randomname")
		self.assertEqual(response, 'User has been successfully created.')

	def test_password_hash(self):
		response = self.user.password_hash('mwalugha')
		self.