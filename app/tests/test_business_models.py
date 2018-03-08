import unittest
from ..models.business import Business


#from ..app.models.user import User

class UserModelTestCase(unittest.TestCase):
	def setUp(self):
		self.business = Business()

	def tearDown(self):
		self.business = None

	def test_register_business(self):
		response = self.business.register_business("Mama Mboga", "Kibera", "Sole Proprietorship", "I sell the best vegetables in town.")
		self.assertEqual(response, "Business has been successfully created.")