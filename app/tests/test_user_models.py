import unittest
from ..models.user import User


#from ..app.models.user import User

class UserModelTestCase(unittest.TestCase):
	def setUp(self):
		self.user = User()

	def test_create_user(self):
		response = self.user.create_user("John", "john@gmail.com", "randomname", "randomname")
		self.assertEqual(response, 'User has been successfully created.')

	def test_password_salts_are_random(self):
		u = self.user.password_hash('cat')
		u2 = self.user.password_hash('cat')
		self.assertTrue(u != u2)