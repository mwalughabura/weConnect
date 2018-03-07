import unittest
from app.models import User

class UserModelTestCase(unittest.TestCase):
	def setUp(self):
		self.user = User()

	def test_create_user(self):
		response = self.user.create_user(self, "John", "john@gmail.com", "randomname", "randomname")
		self.assertEqual(response, 'User has been successfully created.')

	# def test_password_setter(self):
	# 	u = User(password = 'cat')
	# 	self.assertTrue(u.password_hash is not None)


	# def test_no_password_getter(self):
	# 	u = User(password = 'cat')
	# 	with self.assertRaises(AttributeError):
	# 		u.password


	# def test_password_verification(self):
	# 	u = User(password = 'cat')
	# 	self.assertTrue(u.verify_password('cat'))
	# 	self.assertFalse(u.verify_password('dog'))